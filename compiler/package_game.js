// Package validated Python + converted TypeScript in MakeCode's PNG format.
// Format: microsoft/pxt pxtlib/util.ts (imageMagic/imageHeaderSize/encodeBlobAsync).
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const arcade = fs.realpathSync(path.dirname(require.resolve('pxt-arcade/package.json', {paths: [__dirname]})));
const core = path.dirname(require.resolve('pxt-core/package.json', {paths: [arcade]}));
const {PNG} = require(require.resolve('pngjs', {paths: [core]}));
const lzma = require(require.resolve('lzma', {paths: [core]}));
const MAGIC = 0x59347a7d;
const HEADER = 36;
const pngPath = fs.existsSync(path.join(root,'Find-My-Drum-Audio-project.png'))
    ? path.join(root,'Find-My-Drum-Audio-project.png')
    : path.join(root,'Find-My-Drum-project.png');

function decode(picture) {
    const pixels = picture.data;
    const bpp = (pixels[0] & 1) | ((pixels[1] & 1) << 1) | ((pixels[2] & 1) << 2);
    if (bpp < 1 || bpp > 4) throw Error('Invalid cartridge bits per channel');
    function read(ptr, bits, size) {
        const output = Buffer.alloc(size);
        let shift = 0, acc = 0, index = 0;
        const mask = (1 << bits) - 1;
        while (index < size) {
            acc |= (pixels[ptr++] & mask) << shift;
            if ((ptr & 3) === 3) ptr++;
            shift += bits;
            if (shift >= 8) {
                output[index++] = acc & 255;
                acc >>>= 8;
                shift -= 8;
            }
        }
        return {output, ptr};
    }
    const header = read(4, bpp, HEADER);
    if (header.output.readUInt32LE(0) !== MAGIC) throw Error('Invalid cartridge magic');
    const size = header.output.readUInt32LE(4), added = header.output.readUInt32LE(8);
    if (added) throw Error('Unsupported overflow rows');
    return read(header.ptr, bpp, size).output;
}

function encode(picture, compressed) {
    const pixels = picture.data;
    let bpp = 1;
    while (((picture.width * picture.height - 1) * 3 * bpp >> 3) < HEADER + compressed.length) bpp++;
    if (bpp > 4) throw Error('Project exceeds cartridge capacity');
    for (let channel = 0; channel < 3; channel++) pixels[channel] = (pixels[channel] & 254) | ((bpp >> channel) & 1);
    function write(ptr, data) {
        const mask = (1 << bpp) - 1;
        for (let bitIndex = 0; bitIndex < data.length * 8; bitIndex += bpp) {
            let bits = 0;
            for (let bit = 0; bit < bpp; bit++) {
                const index = bitIndex + bit;
                if (index < data.length * 8) bits |= ((data[index >> 3] >> (index & 7)) & 1) << bit;
            }
            pixels[ptr] = (pixels[ptr] & ~mask) | bits;
            ptr++;
            if ((ptr & 3) === 3) pixels[ptr++] = 255;
        }
        return ptr;
    }
    const header = Buffer.alloc(HEADER);
    header.writeUInt32LE(MAGIC, 0);
    header.writeUInt32LE(compressed.length, 4);
    write(write(4, header), compressed);
    for (let alpha = 3; alpha < pixels.length; alpha += 4) pixels[alpha] = 255;
    return PNG.sync.write(picture);
}

function compress(source) {
    return new Promise((resolve, reject) => lzma.compress(source, 1, (result, error) => error ? reject(error) : resolve(Buffer.from(result))));
}
function decompress(source) {
    return new Promise((resolve, reject) => lzma.decompress(Array.from(source), (result, error) => error ? reject(error) : resolve(result)));
}

async function main() {
    const source = fs.readFileSync(path.join(root, 'main.py'), 'utf8');
    const report = JSON.parse(fs.readFileSync(path.join(__dirname, 'results/compile-report.json'), 'utf8'));
    const sourceHash = crypto.createHash('sha256').update(source).digest('hex');
    if (!report.success || report.diagnostics.length || report.sourceSha256 !== sourceHash) throw Error('Compile current source before packaging');
    // The cartridge's artwork stays intact; replace its embedded project files.
    const picture = PNG.sync.read(fs.readFileSync(pngPath));
    const files = {
        'pxt.json': JSON.stringify({name:'Find My Drum - Audio Edition', dependencies:{device:'*'}, files:['main.py','main.ts'], preferredEditor:'pyprj', targetVersions:{target:'4.1.25'}}),
        'main.py': source,
        'main.ts': fs.readFileSync(path.join(__dirname,'results/main.ts'),'utf8')
    };
    const project = {meta:{name:'Find My Drum - Audio Edition',editor:'pyprj',cloudId:'pxt/arcade',target:'arcade',targetVersions:{target:'4.1.25'}},source:JSON.stringify(files)};
    // Verify the exact exported file set, including the Python editor preference.
    require(path.join(core,'built/pxt.js'));
    const {pxt,pxtc} = global;
    pxt.setAppTarget(JSON.parse(fs.readFileSync(path.join(arcade,'built/target.json'),'utf8')));
    const options = await pxt.simpleGetCompileOptionsAsync(files,{native:false});
    options.target.isNative=false;
    options.target.preferredEditor=pxt.PYTHON_PROJECT_NAME;
    const packagedCompile=pxtc.compile(options);
    if (!packagedCompile.success || packagedCompile.diagnostics.length) {
        throw Error('Exported project does not compile: ' + packagedCompile.diagnostics.map(d=>pxtc.getDiagnosticString(d)).join('\n'));
    }
    const compressed = await compress(JSON.stringify(project));
    const output = encode(picture, compressed);
    const roundtrip = JSON.parse(await decompress(decode(PNG.sync.read(output))));
    if (roundtrip.source !== project.source) throw Error('Project payload roundtrip mismatch');
    const destination = path.join(root, 'Find-My-Drum-Audio-project.png');
    fs.writeFileSync(destination, output);
    const packageReport = {sourceSha256:sourceHash,cartridgeSha256:crypto.createHash('sha256').update(output).digest('hex'),payloadRoundtripPassed:true,exportedProjectCompilePassed:true,projectFiles:Object.keys(files),importRuntimeVerified:false};
    fs.writeFileSync(path.join(__dirname,'results/package-report.json'),JSON.stringify(packageReport,null,2));
    console.log('Packaged:', destination);
    console.log(JSON.stringify(packageReport,null,2));
}
main().catch(error => {console.error(error.stack); process.exitCode=1;});
