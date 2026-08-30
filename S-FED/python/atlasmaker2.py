def write_to_file(filename):
    vgate_values = [round(-0.1 + i * 0.1, 1) for i in range(0 , 15)]  # Sweep vgate from -0.1 to 1.1 in steps of 0.1
    vwell_values = [round(-0.1 + i * 0.1, 1) for i in range(0 , 15)]  # Sweep vwell from -0.1 to 1.1 in steps of 0.1

    with open(filename, 'w') as file:
        for well_index, vwell in enumerate(vwell_values):
            for gate_index, vgate in enumerate(vgate_values):
                mode_id = f"{well_index:02}_{gate_index:02}"
                file.write(f"#*****************ID VD Mode {mode_id} ************************************* \n")
                file.write(f"log          outf=sfedMode{mode_id}.log  \n")
                file.write("solve        vdrain=0\n")
                file.write("solve        vbulk=$VDDmid\n")
                file.write("solve        vsource=0\n")
                file.write(f"solve        vwell={vwell}\n")
                file.write(f"solve        vgate={vgate} \n")
                #file.write("solve        vdrain=0 vstep=0.01 name=drain vfinal=$VDD\n")
                file.write("solve        vdrain=-0.1 vstep=0.01 name=drain vfinal=1.3\n")

# Specify the filename and write the content
def main():
    output_file = "C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/S-FED DR_2/sweep_output.txt"
    write_to_file(output_file)
    print(f"Content written to {output_file}")

if __name__ == "__main__":
    main()
