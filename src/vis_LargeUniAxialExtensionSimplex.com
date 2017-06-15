# read in solution, which may be split into multiple files
@exnodes=<./LargeUniaxialExtensionSimplex.part0.exnode>;
@exelems=<./LargeUniaxialExtensionSimplex.part0.exelem>;
foreach $filename (@exnodes) {
    print "Reading $filename\n";
    gfx read node "$filename";
}
foreach $filename (@exelems) {
    print "Reading $filename\n";
    gfx read elem "$filename";
}

# display undeformed lines
gfx define faces egroup "Region"
gfx modify g_element Region general clear;
gfx modify g_element "Region" lines select_on material green selected_material default_selected

gfx create window 1

gfx modify g_element "/" point glyph axes general size "1.2*1.2*1.2" material default selected_material default_selected;
# nodes as spheres, radius 0.1
gfx modify g_element Region node_points glyph sphere size 0.1 label cmiss_number select_on material default selected_material default_selected


gfx modify window 1 set antialias 2
