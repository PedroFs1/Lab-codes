dir = getDirectory("Choose a folder");
list = getFileList(dir);

for (i = 0; i < list.length; i++) {

    open(dir + list[i]);
    
	run("16-bit");
	run("Set Scale...", "distance=0 known=0 pixel=1 unit=pixel global");
	run("Despeckle");
	run("Subtract Background...", "rolling=20");
	setThreshold(27, 6255);
	run("Set Measurements...", "area limit redirect=None decimal=1");
	run("Measure"); 
	}
close("*");
	