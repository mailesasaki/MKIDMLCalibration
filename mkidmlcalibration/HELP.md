1. You'll want to double check the mlDict file and make sure that the model directory, name of the ML model, and training file directory are as you like. Also, if you have a trainNPZ file, have the name in there, too.
2. $ mkdir "trainFileDir" to contain the npz files
3. scp sweep npz files into the above directory.
4. $ conda activate mkidcal 
5. If there's no ml model yet, train a model using: python train_model.py /path/to/mldictfile.yml
   1. The ML model will have also have graphs of the training and validation accuracy and loss inside.
7. Run ML inference script using: python findResonatorsWPS.py /path/to/mlmodel/fullval_final_1 /path/to/sweep/npz -o /path/to/metadata/output
   i. If your computer doesn't have 8 or more CPUs, you can run it with 1 CPU instead.
   ii. The paths (for sweep npz and metadata out) use format tags {roach}, {feedline}, and {range}, which behave the same way as they do in the templar/dashboard config files
   iii. After metadata files are completed we want to look at the histograms of the powers and clip off the lowest attenuations (highest powers). This will increase the dynamic range of the ADC/DAC and improve performance
7. Navigate to mkidreadout/configuration
8. Run python processResLists.py --clip-atten /path/to/metadata_{roach}_fl{feedline}{range}.txt -s /path/to/psData_{roach}.npz --find-lo --config /path/to/roach.yml --clip-atten --flag <flag>
This script will do the following:
   i. If the “find-lo” option is used, it will find the a and b LOs for each feedline, and write them to the roach.yml specified by the --config argument. This will OVERWRITE the config file. This should generally always be done when the ML fitting code is used to generate new metadata lists.
   ii. If the “--clip-atten” option is used, it will pop up a gui showing histograms of the attenuations. Clicking the gui will move the blue bars bounding the histogram and change the max and min attenuation values. The general rule of thumb is to lop off 5dB from the low attenuation side.
   iii. Optionally, the “--freq-shift” option may be used to add a global shift to all the resonators. We often use -30 kHz.
   iv. When finished, the new metadata will be saved to a file with the same name as the metadata file + ‘_<flag>.txt’. 

