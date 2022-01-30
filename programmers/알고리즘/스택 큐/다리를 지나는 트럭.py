def solution(bridge_length, weight, truck_weights):
    cnt = 0
    # [트럭 무게, 이동거리]
    calc_truck = [[t, i] for i, t in zip([0] * len(truck_weights), truck_weights)]

    # 다리 위에 있는 버스
    above_bridge = []

    # 도착한 버스
    arrived_truck = []
    all_truck = len(truck_weights)

    while True:
        # 모든 트럭이 도착할 때 종료
        if all_truck == len(arrived_truck):
            break

        for i in range(len(above_bridge)):
            above_bridge[i][1] = above_bridge[i][1] + 1

        # 다리 위 총 무게가 이해일때 추가
        all_weight = [c[0] for c in above_bridge]
        if (sum(all_weight) + calc_truck[0][0]) <= weight:
            truck = calc_truck.pop(0)
            above_bridge.append(truck)


        # 다리 위 트럭이 도착할 때 : 차 빼기
        if len(above_bridge) > 0 and above_bridge[0][1] == bridge_length:
            truck = above_bridge.pop(0)
            arrived_truck.append(truck)

        cnt += 1

    return cnt

print(solution(2, 10, [7,4,5,6]))
