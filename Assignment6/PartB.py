def calName(name):
    name = name.upper()
    crnum = [0] * 255
    sum = 0
    for i in range(ord("A"), ord("Z") + 1):
        crnum[i] = (i - ord("A") + 1) % 9
        if crnum[i] == 0:
            crnum[i] = 9  
    for i in range(len(name)):
        sum += crnum[ord(name[i])]
    while sum > 9 and sum != 11 and sum != 22:
        tsum = 0
        for i in range(len(str(sum))):
            tsum += int(str(sum)[i])
        sum = tsum
    return sum

def npa(sum):
    strname = {
        1: "initiating action, pioneering, leading, independent, attaining, individual",
        2: "cooperation, adaptability, consideration of others, partnering, mediating",
        3: "expression, verbalization, socialization, the arts, the joy of living",
        4: "a foundation, order, service, struggle against limits, steady growth",
        5: "expansiveness, visionary, adventure, the constructive use of freedom",
        6: "responsibility, protection, nurturing, community, balance, sympathy",
        7: "analysis, understanding, knowledge, awareness, studious, meditating",
        8: "practical endeavors, status oriented, power seeking, material goals",
        9: "humanitarian, giving nature, selflessness, obligations, creative expression",
        11: "higher spiritual plane, intuitive, illumination, idealist, a dreamer",
        22: "the Master Builder, large endeavors, powerful force, leadership"
    }
    return strname.get(sum, None)

if __name__ == "__main__":
    name = input("Enter your name: ")
    print("Your Personality number is: " + str(calName(name)))  
    print("Your personality associations are:")
    print(npa(calName(name)))