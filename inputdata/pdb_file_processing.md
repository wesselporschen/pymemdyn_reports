## .pdb file preparation before PyMemDyn
Written here is a description of how each of the `.pdb` structures was acquired, which modifications were present, and how they were processed before membrane embedding with PyMemDyn.

1. **5OLZ (A2AAR, from Deflorian 2020)**
*Mutation / WT?:* Star2-bRIL562
*Pre-processed structure available?:* Yes, from [Ross benchmark set](https://github.com/schrodinger/public_binding_free_energy_benchmark/tree/main)

*Modifications / mutations in structure (from methods section, p. 5567):*
- StaR2 mutation (A54L2.52, T88A3.36, R107A3.55, K122A4.43, L202A5.63, L235A6.37, V239A6.41 and S277A7.42). Not reverted by Deflorian 2020.
- Removal of glycosilation site (N154A). Not reverted by Deflorian 2020.
- bRIL insertion between helices 5 and 7. Reverted by Deflorian (but loop not explicitly rebuilt in pre-processed structure... gap presumably filled by MODELLER during PyMemDyn-step).
- C-terminal decahistidine tag. Reverted by Deflorian 2020.

The co-crystallized ligand of 5OLZ (T4E) was missing from the pre-processed structure. I added it back from the accompanying `.sdf` ligand series and checked the position based on T4E's original position in the 5OLZ structure from Protein Data Bank.

2. **4S0V (OX2, from Deflorian 2020)**
*Mutation / WT?*: Fusion protein inserted between Q205 - K209.
*Pre-processed structure available?:* Yes, from [Ross benchmark set](https://github.com/schrodinger/public_binding_free_energy_benchmark/tree/main)

*Modifications / mutations in structure (from methods section, p. 5567)*
- Fusion protein inserted between Q205 - K209. Removed by Deflorian 2020. Loop was closed with three Gly residues to link helices 5 and 6.
- Extracellular loop 2 (ECL2) was not fully resolved and was modeled based on the OX1 structure 4ZJ8.

Added co-crystallized ligand SUV from original 4S0V structure by aligning it with the pre-processed structure and adding SUV to the pre-processed structure. (`align` in PyMol). Protonated the ligand with PyMol.

3. **4XNV (P2Y1, from Dickson 2021)**
*Mutation / WT?*: rubredoxin insert between K247, and P253. Point mutation D320N.
*Pre-processed structure available?:* Yes, from [Ross benchmark set](https://github.com/schrodinger/public_binding_free_energy_benchmark/tree/main)

*Modifications / mutations in structure*
- Dickson 2021 made no mention of reverting mutations. I reverted the D320N point mutation.
- Evident in the structure, they did remove the rubredoxin31 insert between K247 and P253 in ICL3 of the P2Y1R protein. But they did not fill in the broken loop, but solved this by placing ACE and NME capping groups. I removed them: breaks will be filled in with poly-A by MODELLER during PyMemDyn.

*Note:* In the Ross benchmark set, the ortho- and meta-substituted ligands are treated separately: 2 ligand subsets with 2 (almost identical) structures. In the Dickson 2021 study, however, all ligands are connected in the same perturbation map (which includes the co-crystallized BUR), also only 1 `.pdb` structure was used for FEP. Therefore, I will just use 1 structure (`ortho`-structure from the Ross benchmark set).

Added the co-crystallized ligand BUR from original 4XNV structure from PDB by aligning it with the pre-processed 4XNV structure (`align` in PyMol). Protonated BUR with PyMol.

4. **2RH1 (Beta 2 Adren. R, from Panel 2023)**
*Mutation / WT?*: T4L lysozyme insert in ICL3.
*Pre-processed structure available?*: No. Used 2RH1 structure from PDB.

*Modifications / mutations in structure*
Panel 2023 states "Engineered mutations were reverted" (Supp Info). According to structure source (Cherezov 2007), the following mutations / modifications were present:
- T4 lysozyme insertion in ICL3 between amino acids 232 and 262. Removed by me, missing loop section filled in by poly A by MODELLER during PyMemDyn-step.
- N terminus (aa 1-28), C-terminus (aa 342-365) not resolved in structure. These termini are kept absent from structure, will not be added by me / MODELLER.
- Palmitic acid covalently bound to Cys-341, acetamide bound to Cys-265. These structures were manually removed by me.

Co-crystallized ligand CAU was protonated using PyMol. Protein structure will be protonated during PyMemDyn-step.

5. **4EIY (A2AAR, from Matricon 2017)**
*Mutation / WT?*: bRIL insert in ICL3.
*Pre-processed structure available?*: No, used 4EIY structure from PDB.

*Modifications / mutations in structure*
Matricon 2017 gives no information about processing of 4EIY structure (e.g. bRIL-reversion). According to structures source (Liu 2012) the following mutations / modifications were present:
- Ala-1 to Leu-106 of bRIL were inserted between Lys-209 to Gly-218 within the A2AAR" (Supp Info). This bRIL insert was removed by me, missing loop section filled in by Poly A by MODELLER during PyMemDyn-step.
- C-terminal residues aa 317-412 were truncated. These were kept as truncated and not rebuilt by me / MODELLER.

Ligand ZMA protonated in PyMol. Protein structure protonated automatically in PyMemDyn-step.

6. **5OLO (A2AAR, from Matricon 2021)**
*Mutation / WT?:* Star2-bRIL562 (same source as 5OLZ)
*Pre-processed structure available?:* No, used 5OLO structure from PDB.

*Modifications / mutations in structure*
Matricon 2021 states "engineered mutations were reverted, non-protein atoms were removed prior to membrane" (Supp Info). I closely followed the processing steps / reversions found in the pre-processed 5OLO structure.
- Manually removed extra aa's on N terminus (such that sequence starts at aa=1 according to UniProt sequence)
- Amino acids 306-412 (C terminus) were not resolved in structure. Were not rebuilt by me / MODELLER.
- bRIL562 insert between transmembrane helices 5 and 6. Manually removed. Missing loop section filled by poly A by MODELLER during PyMemDyn.
- Glycosilation site removal mutation: N154A. Not removed by me due to conflicting residues.
- StaR2 mutations (A54L2.52, T88A3.36, R107A3.55, K122A4.43, L202A5.63, L235A6.37, V239A6.41 and S277A7.42). Reverted by me with PyMol mutagenesis tool. 

Co-crystallized ligand 9XW protonated with PyMol. Protein structure protonated during PyMemDyn-step.

### Co-crystallized waters (structures `2RH1`, `4EIY`, and `5OLO`)
Some structures (`2RH1`, `4EIY`, and `5OLO`) contained co-crystallized water molecules. Because 1) these can influence binding behavior of the ligand, and 2) to follow the methods of the respective FEP-studies as closely as follows, these were included during the PyMemDyn membrane insertion (flag `-w`). Briefly,
1. All water molecules outside of the GPCR protein were removed.
2. The remaining intra-helical water molecules were protonated in PyMol
3. Then, they were extracted from the structure `.pdb` into a separate file (e.g. `2RH1_waters.pdb`)
4. In PyMemDyn, they were included as follows: `pymemdyn -p 2RH1_complex_rdy.pdb -l CAU -i NA -w 2RH1_waters.pdb`
