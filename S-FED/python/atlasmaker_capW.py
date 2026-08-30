def write_to_file(filename):
    vdrain_values = [round(-0.4 + i * 0.1, 1) for i in range(0 , 21)]  # Sweep vdrain from -0.4 to 1.6 in steps of 0.1
    vgate_values = [round(-0.4 + i * 0.1, 1) for i in range(0 , 21)]  # Sweep vgate from -0.4 to 1.6 in steps of 0.1

    with open(filename, 'w') as file:
        for gate_index, vgate in enumerate(vgate_values):
            for drain_index, vdrain in enumerate(vdrain_values):
                mode_id = f"{gate_index:02}_{drain_index:02}"
                file.write(f"#*****************ID VD Mode {mode_id} ************************************* \n")
                file.write("solve        vwell=0\n")
                file.write("solve        vbulk=$VDDmid\n")
                file.write("solve        vsource=0\n")
                file.write(f"solve        vgate={vgate}\n")
                file.write(f"solve        vdrain={vdrain} \n")
                file.write("#-0.5 baraye ine ke on avalesh data ha cherotoperte dar asl ma ba -0.4 ta 16 kar darim faghat\n")
                file.write("solve        name=well vfinal=-0.5 vstep=-0.05 qscv\n")
                file.write(f"log          outf=sfedMode{mode_id}.log  \n")
                file.write("solve        name=well vfinal=1.6 vstep=0.05 qscv\n")
                file.write("log off\n")

# Specify the filename and write the content
def main():
    output_file = "C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/S-FED DR_capW/sweep_capacitance.txt"
    write_to_file(output_file)
    print(f"Content written to {output_file}")

if __name__ == "__main__":
    main()
