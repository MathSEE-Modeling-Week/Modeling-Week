import umbridge

model = umbridge.HTTPModel("http://localhost:4243", "posterior")

one_row_list = [[0 for _ in range(model.get_input_sizes()[0])]]

model(one_row_list)
