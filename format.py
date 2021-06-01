unformatted_file = "./wider_face_train_bbx_gt.txt"
output_file = "./labels.txt"

with open(unformatted_file) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

new_lines = []

for i in range(len(lines)):
    line = lines[i]

    if line[-3:] == 'jpg':
        new_lines.append(line)
    else:
        num_words = len(line.split(' '))
        if num_words > 1:
            new_lines.append(line)

with open(output_file, "w") as f:
    for line in new_lines:
        f.write(line + "\n")