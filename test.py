from identifiability_of_direct_effect_in_scg import *
if __name__ == "__main__":
    gamma_xy = 1
    gamma_max = 2

    ascg_1 = nx.DiGraph()
    ascg_1.add_edge("X", "Y")
    ascg_1.add_edge("X", "U")
    ascg_1.add_edge("U", "Z")
    ascg_1.add_edge("Z", "W")
    ascg_1.add_edge("W", "Y")

    ascg_2 = nx.DiGraph()
    ascg_2.add_edge("X", "Y")
    ascg_2.add_edge("U", "X")
    ascg_2.add_edge("Z", "U")
    ascg_2.add_edge("Z", "W")
    ascg_2.add_edge("W", "Y")

    ascg_3 = nx.DiGraph()
    ascg_3.add_edge("X", "Y")
    ascg_3.add_edge("X", "U")
    ascg_3.add_edge("U", "Z")
    ascg_3.add_edge("W", "Z")
    ascg_3.add_edge("Y", "W")

    list_ascgs = [ascg_1, ascg_2, ascg_3]

    def add_fixed_edges(scg):
        scg.add_edges_from([("X", "X"), ("Y", "Y"), ("U", "U"), ("W", "W"), ("Z", "Z")])
        scg.add_edge("X", "Y")
        scg.add_edge("X", "U")
        scg.add_edge("U", "X")
        scg.add_edge("Y", "W")
        scg.add_edge("W", "Y")

    scg1_1 = nx.DiGraph()
    add_fixed_edges(scg1_1)
    scg1_1.add_edge("U", "Z")
    scg1_1.add_edge("Z", "W")

    scg1_2 = nx.DiGraph()
    add_fixed_edges(scg1_2)
    scg1_2.add_edge("U", "Z")
    scg1_2.add_edge("Z", "U")
    scg1_2.add_edge("Z", "W")

    scg1_3 = nx.DiGraph()
    add_fixed_edges(scg1_3)
    scg1_3.add_edge("U", "Z")
    scg1_3.add_edge("Z", "W")
    scg1_3.add_edge("W", "Z")

    scg1_4 = nx.DiGraph()
    add_fixed_edges(scg1_4)
    scg1_4.add_edge("U", "Z")
    scg1_4.add_edge("W", "Z")

    scg1_5 = nx.DiGraph()
    add_fixed_edges(scg1_5)
    scg1_5.add_edge("Z", "U")
    scg1_5.add_edge("Z", "W")

    list_scgs_identifiable = [scg1_1, scg1_2, scg1_3, scg1_4, scg1_5]

    scg2_1 = nx.DiGraph()
    add_fixed_edges(scg2_1)
    scg2_1.add_edge("Z", "U")
    scg2_1.add_edge("W", "Z")

    scg2_2 = nx.DiGraph()
    add_fixed_edges(scg2_2)
    scg2_2.add_edge("Z", "U")
    scg2_2.add_edge("W", "Z")
    scg2_2.add_edge("Z", "W")

    scg2_3 = nx.DiGraph()
    add_fixed_edges(scg2_3)
    scg2_3.add_edge("Z", "U")
    scg2_3.add_edge("U", "Z")
    scg2_3.add_edge("W", "Z")

    list_scgs_identifiable_with_cond = [scg2_1, scg2_2, scg2_3]

    scg3_1 = nx.DiGraph()
    add_fixed_edges(scg3_1)
    scg3_1.add_edge("Z", "U")
    scg3_1.add_edge("U", "Z")
    scg3_1.add_edge("W", "Z")
    scg3_1.add_edge("Z", "W")

    list_scgs_not_identifiable = [scg3_1]

    print("ASCGs")
    for ascg in list_ascgs:
        res = is_identifiable(ascg, "X", "Y", gamma_xy, gamma_max=gamma_max)
        print(ascg.edges)
        print(res)
        if res:
            print(sorted(adjustment_set_for_direct_effect_in_ascgl(ascg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
            print(sorted(huge_adjustment_set_for_direct_effect_in_scg(ascg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
            print(sorted(smaller_adjustment_set_for_direct_effect_in_scg(ascg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))

    print("Identifiable SCGs")
    for scg in list_scgs_identifiable:
        res = is_identifiable(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)
        print(scg.edges)
        print(res)
        if res:
            print(sorted(huge_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
            print(sorted(smaller_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))

    print("Identifiable SCGs if gamma_xy >0")
    for scg in list_scgs_identifiable_with_cond:
        res = is_identifiable(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)
        print(scg.edges)
        print(res)
        if res:
            print(sorted(huge_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
            print(sorted(smaller_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))

    print("Not identifiable SCGs")
    for scg in list_scgs_not_identifiable:
        res = is_identifiable(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)
        print(scg.edges)
        print(res)
        if res:
            print(sorted(huge_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
            print(sorted(smaller_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))

    special_scg = nx.DiGraph()
    add_fixed_edges(special_scg)
    special_scg.add_edge("Y", "X")

    special_scg2 = nx.DiGraph()
    add_fixed_edges(special_scg2)
    special_scg2.remove_edge("X", "U")
    special_scg2.remove_edge("X", "X")
    special_scg2.add_edge("Y", "X")

    list_special_scgs = [special_scg, special_scg2]

    print("Special SCGs: expected results = False, True")
    for scg in list_special_scgs:
        res = is_identifiable(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)
        print(scg.edges)
        print(res)
        if res:
            print(sorted(huge_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
            print(sorted(smaller_adjustment_set_for_direct_effect_in_scg(scg, "X", "Y", gamma_xy, gamma_max=gamma_max)[1]))
