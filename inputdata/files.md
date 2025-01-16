## Ligand parameters
Due to difficulty with the on-server installation of LigParGen, the ligand parameters were generated with an online server:
- https://traken.chem.yale.edu/ligpargen/
- Ref: LigParGen web server: An automatic OPLS-AA parameter generator for organic ligands. Dodda, L. S.;Cabeza de Vaca, I.; Tirado-Rives, J.; Jorgensen, W. L. Nucleic Acids Research, Volume 45, Issue W1, 3 July 2017, Pages W331-W336

---
OPLS-AA parameters with 1.14\*CM1A partial atomic charges

input: `.pdb` file of ligand (e.g. '9XW'), extracted from protein-ligand crystal structure (e.g. '5OLO', from PDB).

output: openMM `.pdb`-file & GROMACS TOP `.itp`-file

## Files
1. `PDB_complex_rdy.pdb`: Complete, pre-processed protein structure containing all ligands, ions, and co-crystallized watermolecules. Used for PyMemDyn membrane embedding (`-p`)
2. `PDB_LIG.pdb`: Ligand extracted from protein structure (1). Used as input in LigParGen web server.
3. `PDB_LIG_openmm.pdb`: OpenMM coordinate file. Output from LigParGen web server. Used for PyMemDyn membrane embedding (`-l`, needs to be renamed to `LIG.pdb` first).
4. `PDB_LIG_gromacstop.itp`: GROMACS topology file. Output from LigParGen web server. Used for PyMemDyn membrane embedding (`-l`, needs to be renamed to `LIG.itp` first).
5. `PDB_waters.pdb`: if co-crystallized water molecules were present in the structure, the intrahelical waters were extracted to a separate file to be included with the `-w` flag.

