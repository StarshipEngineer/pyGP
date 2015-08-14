import pygp

def tournament(population, n, data):
    """Performs tournament selection, randomly choosing n individuals from the
    population and thunderdome-ing it, returning the individual with the best
    fitness
    """
    pop_sample = _sample(population, n)
    best = None
    best_score = None
    for item in pop_sample:
        try:
            score = fitness(item, data)
            if (best_score == None) or (score < best_score):
                best = item
                best_score = score
            #
            print("tree:", pygp.display(item))
            print("score", score)
            #
        except SingularityError:
            pass
        except UnfitError:
            pass
    print("best:", pygp.display(best))
    return best
