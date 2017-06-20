

def get_pie_slices():
    pie = 100
    slices = {}
    people = 100
    for person in range(1, people + 1):
            slice = pie * (person * 0.01)
            slices[person] = slice
            pie = pie - slice
    return slices


def get_max_slice(slices):
    max = 0
    max_value_index = 0
    for slice_value in slices:
        if slices[slice_value] > max:
            max = slices[slice_value]
            max_value_index = slice_value
    return (max_value_index, max)


pie_slices = get_pie_slices()
max_slice = get_max_slice(pie_slices)
print("Person %s gets the largest slice of %s, because reasons." % (max_slice[0], max_slice[1]))
