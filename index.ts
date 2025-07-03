import sqlite from 'node:sqlite';

const db = new sqlite.DatabaseSync('out.gpkg', {'readOnly': true})

const contentsStmt = db.prepare(
"SELECT table_name, srs_id FROM gpkg_contents WHERE data_type = 'features' LIMIT 1"
);
const contents = contentsStmt.get();
console.log('Contents:', contents);