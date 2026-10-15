// Official MakeCode Python converter + Arcade simulator compiler, offline.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const arcade = fs.realpathSync(path.dirname(require.resolve('pxt-arcade/package.json', { paths: [__dirname] })));
const core = path.dirname(require.resolve('pxt-core/package.json', { paths: [arcade] }));
require(path.join(core, 'built/pxt.js'));
const { pxt, pxtc } = global;
const target = JSON.parse(fs.readFileSync(path.join(arcade, 'built/target.json'), 'utf8'));
pxt.setAppTarget(target);
const results = path.join(__dirname, 'results');
fs.mkdirSync(results, { recursive: true });

async function main() {
    const source = fs.readFileSync(path.join(root, 'main.py'), 'utf8');
    const files = {
        'pxt.json': JSON.stringify({
            name: 'Find My Drum',
            dependencies: { device: '*' },
            files: ['main.py'],
            preferredEditor: 'pyprj'
        }),
        'main.py': source
    };
    // SimpleHost reads dependencies from target.bundledpkgs; no network install.
    const options = await pxt.simpleGetCompileOptionsAsync(files, { native: false });
    options.target.isNative = false;
    options.target.preferredEditor = pxt.PYTHON_PROJECT_NAME;
    // compile() calls the official Python->TS conversion when editor is pyprj.
    const result = pxtc.compile(options);
    const diagnostics = (result.diagnostics || []).map(d => ({
        code: d.code,
        category: d.category,
        fileName: d.fileName,
        line: d.line,
        column: d.column,
        message: pxtc.getDiagnosticString(d)
    }));
    for (const [filename, content] of Object.entries(result.outfiles || {})) {
        const destination = path.resolve(results, filename);
        if (!destination.startsWith(results + path.sep)) throw Error('Invalid compiler output path');
        fs.mkdirSync(path.dirname(destination), { recursive: true });
        fs.writeFileSync(destination, content);
    }
    const report = {
        target: 'arcade',
        targetVersion: require(path.join(arcade, 'package.json')).version,
        compilerVersion: require(path.join(core, 'package.json')).version,
        mode: 'official_python_to_typescript_and_simulator_compile',
        sourceSha256: crypto.createHash('sha256').update(source).digest('hex'),
        success: result.success,
        diagnostics,
        outfiles: Object.keys(result.outfiles || {}),
        checkedAt: new Date().toISOString(),
        runtimeVerified: false
    };
    fs.writeFileSync(path.join(results, 'compile-report.json'), JSON.stringify(report, null, 2));
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = result.success && !diagnostics.length ? 0 : 1;
}
main().catch(error => { console.error(error.stack); process.exitCode = 1; });
