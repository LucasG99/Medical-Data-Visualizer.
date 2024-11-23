from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate and save the cat plot
cat_plot = draw_cat_plot()
cat_plot.savefig("catplot.png")

# Generate and save the heat map
heat_map = draw_heat_map()
heat_map.savefig("heatmap.png")