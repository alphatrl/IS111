def find_stations_within_distance(mrt_map, orig, dist):
    # Modify the code below

    journey_list = []

    # if distance == 1, look for neighbouring mrt and append to journey_list
    for line in mrt_map:
      if orig in line:
        index = line.index(orig)

        # get neighbour mrt stations
        index_back = index - 1
        index_front = index + 1

        if dist == 1:
          if index_back >= 0:
            journey_list.append(line[index_back])
          if index_front < len(line):
            journey_list.append(line[index_front])

        # go recursive
        else:
          # create new mrt map without current station
          new_mrt_map = []
          new_line = line.copy()
          new_line.remove(orig)

          for temp in mrt_map:
            if temp == line:
              temp = new_line
            new_mrt_map.append(temp)

          if index_back >= 0:
            new_mrt = line[index_back]
            journey_list.append(new_mrt)
            journey_list.extend(find_stations_within_distance(new_mrt_map, new_mrt, dist - 1))

          if index_front < len(line):
            new_mrt = line[index_front]
            journey_list.append(new_mrt)
            journey_list.extend(find_stations_within_distance(new_mrt_map, new_mrt, dist - 1))

    # remove duplicates
    journey_list = list(dict.fromkeys(journey_list))

    return journey_list

