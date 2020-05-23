# Modelling Potential RNA:RNA Interactions Between SARS-CoV-2 and Human Transcriptome

## *Introduction*
The Mod-RNA bioinformatic pipeline, consisting of scripts, linked repositories and example files as described in this README.md, were collaboratively produced by a group of Post-doctoral, Graduate and Undergraduate biologists and computer scientists as part of the [hackseqRNA](https://www.hackseq.com/rna): COVID-19 Ultra-hackathon event, which occurred remotely from May 22 - 24, 2020. Mod-RNA is a bioinformatics pipeline used to integrate SARS-Cov-2 sub-genomic RNA from transcriptome data and RNA secondary structure predictions to generate RNA:RNA interaction network visualizations. 

## *Description*
Given the short timescale between when SARS-Cov-2 was first discovered and when it was designated a pandemic, there is next-to-no high-throughput data for the virus. This precludes in-depth integrative, systems-level analyses on it and as such our understanding of the large-scale effects it has on cellular behaviour are limited. However, there is such data for other coronaviruses, namely the 2003 outbreak strain (which SARS-CoV-2 is believed to be closely related to) and Middle Eastern Respiratory Syndrome (MERS) virus, alongside other less well-documented coronaviruses. Using these data, differential expression analyses and various gene regulatory network construction methods, it may be possible to identify "consensus" modules/pathways that are dysregulated by all coronaviruses, or at least in coronaviruses that are highly related (SARS coronaviruses). Modules/pathways identified this way could then be compared to the current SARS-CoV-2 literature to identify any evidence that these gene sets are dys-regulated during SARS-CoV-2 infection, with the aim of providing better understanding of the life cycle of the virus and how the virus causes COVID-19.

## *Objectives*
1. Integration of the latest SARS-Cov-2 transcriptome and RNA secondary structure data to predict potential pathogen and host miRNA:mRNA interactions;
2. Visualization of predicted miRNA:mRNA network interactions;
3. Production of ViRBase-compatible network dataset; and 
4. Report the findings of our work in an open access preprint.

## Useful Resources 

1. Non-canonical SARS CoV-2 sgRNAs from [UCSC browser deposit](http://genome.ucsc.edu/cgi-bin/hgTables) by Kim et al., 2020 
2. Human 3’UTR [UTRdb database](http://utrdb.ba.itb.cnr.it/) 
3. Human [EnhancerAtlas database](http://www.enhanceratlas.org/)
4. [CD-HIT](http://weizhongli-lab.org/cd-hit/) (Limin F et al., 2012)
5. [ViennaRNA](https://www.tbi.univie.ac.at/RNA/) (Lorenz R et al., 2011)

## Bioinformatics Approach and Tools Used

1. The sequences for 477 non-canonical SARS-Cov-2 sgRNAs (Kim D et al., 2020) were obtained from the [UCSC genome browser](http://genome.ucsc.edu/cgi-bin/hgTables).  Redundant hits were removed using [CD-HIT](http://weizhongli-lab.org/cd-hit/)  to obtain a FASTA file with 148 sgRNA sequences (identity threshold = 99%).   
2. The non-redundant sequences were aligned with RNA secondary structure regions predicted by Rangan R et al. (2020) to obtain secondary structures for the continuous sgRNAs. 
3. The structure of the 200 nucleotides around junction sites for discontinuous sgRNAs were predicted using ViennaRNA’s RNAfold (120 nucleotide window, slide = 40 nucleotides). Structures with MFE < -20 kCal/mol used for further analysis.  
4. HuntMi (Gudyś A et al., 2013) was used to distinguish pre-miRNA hairpins from pseudo hairpins. Details to be added after discussion. 
5. MatureBayes (Gkirtzou K et al., 2010) used to predict miRNAs from pre-miRNAs.
6. Two more tools from ViennaRNA were used (RNAplfold followed by RNAplex) to find viral miRNA:host mRNA interactions.

## Visualization Approach and Tools Used

* Utilizing Cytoscape.js to visualize the network of possible interactions between RNA molecules of the host and viral.
* Using ViennaRNA to plot structure models developed by the pipeline team.
* Parse pipeline output into cytoscape appropriate JSON: [https://github.com/varun-kotipalli/Model_RNA/tree/master/Visualization/parser](https://github.com/varun-kotipalli/Model_RNA/tree/master/Visualization/parser)
* Current development git repo: [https://github.com/taytayp/cytoscape-rna-model](https://github.com/taytayp/cytoscape-rna-model)
* Cytoscape.js page: [https://js.cytoscape.org/](https://js.cytoscape.org/)

## *The Team*
 
Amber Paulson (Team Lead)

### Pipeline Construction Team: 
  * Teresa  
  * Michaela Agapiou   
  * Anna Valyaeva
  * Sanjana Bhatnagar  
  * Christina Akirtava 
  
 ### Visualization/Analysis Team:
  * Jason Laird 
  * Jaspreet Singh 
  * Fatemeh Kiannejad 
  * Mary Chung 
  
### Integrated management Team :
* Salini Konikkat 
* Taylor Falk 
* Clara Smoniewski
* Thomas Ng 
* Varun Kotipalli 

## Prospective Contributors

Development of Mod-RNA occurred under unprecedented circumstances and each member of the team contributed many hours of work to produce this resource. As a result of the SARs-CoV-2 pandemic, many junior scientists are facing unprecedented challenges to continue working in the science fields. If you see value in this work, please consider supporting one of the team members by providing internship, scholarship, mentorship, work-study or employment to continue working on developing Mod-RNA and conducting RNA research. During pandemic, bioinformatic researchers can continue to carry out important research remotely to contribute to many challenges we face as a global society.
The team does not have capacity to provide on-going support for Mod-RNA, and this tool is made available in draft.

## References
1. Gkirtzou K, Tsamardinos I, Tsakalides P, and Poirazi P (2010) MatureBayes: A Probabilistic Algorithm for Identifying the Mature miRNA within Novel Precursors. PLoS One 5(8):e11843. [doi:10.1371/journal.pone.0011843](https://doi.org/10.1371/journal.pone.0011843)
2. Gudyś A, Wojciech Szcześniak M, Sikora M, and Makałowska I (2013) HuntMi: an efficient and taxon-specific approach in pre-miRNA identification. BMC Bioinformatics 14:83. [doi:10.1186/1471-2105-14-83](https://dx.doi.org/10.1186%2F1471-2105-14-83)
3. Kim D, Lee J-Y, Yang J-S, Kim JW, Kim N, and Chang H (2020) The architecture of SARS-Cov-2 transcriptome. Cell 181: 914-921. [doi:10.1016/j.cell.2020.04.011](https://doi.org/10.1016/j.cell.2020.04.011)
4. Limin F, Beifang N, Zhengwei Z, Sitao W, and Weizhong L (2012) CD-HIT: accelerated for clustering the next generation sequencing data. Bioinformatics 28 (23):3150-3152. [doi:10.1093/bioinformatics/bts565](https://doi.org/10.1093/bioinformatics/bts565)
5. Lorenz R, Bernhart SH,Höner zu Siederdissen C, Tafer H,Flamm C, Stadler PF, and HofackerIvo L (2011) ViennaRNA Package 2.0. Algorithms for Molecular Biology, 6:1 26 [doi:10.1186/1748-7188-6-26](http://dx.doi.org/10.1186/1748-7188-6-26)
6. Rangan R, Zheludev IN, Das R.  RNA genome conservation and secondary structure in SARS-CoV-2 and SARS-related viruses. bioRXiv. [doi:10.1101/2020.03.27.012906](https://doi.org/10.1101/2020.03.27.012906)
7. Wu K, Zou J, Chang HY. (2020) RNA-GPS Predicts SARS-CoV-2 RNA Localization to Host Mitochondria and Nucleolus. Bioinformatics. [http://biorxiv.org/lookup/doi/10.1101/2020.04.28.065201](http://biorxiv.org/lookup/doi/10.1101/2020.04.28.065201)
