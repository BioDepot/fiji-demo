run("BigStitcher", "select=define define_dataset=[Automatic Loader (Bioformats based)] project_filename=dataset.xml path=/data/bigstitcher-data/Grid1 exclude=10 pattern_0=Channels pattern_1=Tiles move_tiles_to_grid_(per_angle)?=[Move Tiles to Grid (interactive)] how_to_load_images=[Re-save as multiresolution HDF5] dataset_save_path=/data/bigstitcher-data check_stack_sizes subsampling_factors=[{ {1,1,1}, {2,2,2} }] hdf5_chunk_sizes=[{ {16,16,16}, {16,16,16} }] timepoints_per_partition=1 setups_per_partition=0 use_deflate_compression export_path=/data/bigstitcher-data/dataset");