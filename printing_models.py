# unpreinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left. Move each design to complete_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Pricing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models thta were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) # lista[:] pasa una copia de esa lista y no la lista como tal así evitamos perder la lista original, ojo que hace que memoria y tiempo que afecta en caso de listas grandes
show_completed_models(completed_models)