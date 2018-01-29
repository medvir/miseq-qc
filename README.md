# MiSeq quality control
> Different tools and scripts to trace quality of Illumina MiSeq runs

#[miseq-qc.Rmd](https://github.com/medvir/miseq-qc/blob/master/miseq-qc.Rmd)

## Goal
Display quality performances of past MiSeq runs in a summary file.

## Requirements
In Order to use this R Markdown script, you need to export and save the run_summary files as follows:
* on the MiSeq open *Illumina Sequencing Analysis Viewer*
* Browse -> select desired run folder (*D:\Illumina\MiSeqOutput\yymmdd_…*)
* Refresh
* in Summary tab click *Copy to Clipboard...*
* open Microsoft Excel
* make sure cell A1 is selected and paste values
* save as *yymmdd_M02081_run_summary.xlsx* in desired folder
* *miseq-qc.Rmd* file has to be in that same folder

## Execution
Open *miseq-qc.Rmd* in RStudio and *Knit the current document (⇧⌘K)*
