#==============================================variable========================================================================
inventory = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

box = ["모자","장검","장갑","장화","가죽","코트","망토","방패","편지","책","성냥","횟불","물통","식량","창","단검","활","화살","부싯돌"]

flag = False
#==============================================start========================================================================
while True :
    flag = False

    for i in range(3) :
        print("="*20)

    question1 = input(f"{box}\n상자 안 물건중 챙길 물건을 고르세요.[완료]:")

    if question1 == "완료": break   #if user select done : break while loop

    elif question1 not in box :
        print("물건의 이름이 불일치 합니다.")

    else :
        while True :
            if flag: break

            for i in range(len(inventory)):
                print(i+1,"번칸.",inventory[i])

            question2 = input("저장할 칸을 고르세요.[취소]:")

            if question2 == "취소" : break

            if question2.isdigit() == True :

                if int(question2) not in [1,2,3,4] :
                    print("1 , 2 , 3 , 4 중 하나의 값만 입력하세요.")

                elif 0 not in inventory[int(question2)-1] :
                    while True :
                        question3 = input(f"인벤토리가 가득 찼습니다.\n{inventory[int(question2)-1]}중 교환할 물건을 고르세요[취소].:")

                        if question3 == "취소" : break

                        elif question3 not in inventory[int(question2)-1] :
                            print("물건의 이름이 불일치합니다.")

                        else :
                            variable_index1 = inventory[int(question2)-1].index(question3)
                            variable_index2 = box.index(question1)

                            box[variable_index2] , inventory[int(question2)-1][variable_index1] = inventory[int(question2)-1][variable_index1] , box[variable_index2]
                            print(inventory[int(question2)-1])
                            flag = True
                            break

                else :
                    variable_index1 = inventory[int(question2)-1].index(0)
                    variable_index2 = box.index(question1)

                    box[variable_index2] , inventory[int(question2)-1][variable_index1] = inventory[int(question2)-1][variable_index1] , box[variable_index2]
                    print(inventory[int(question2)-1])
                    break

            else :
                print("1 , 2 , 3 , 4 중 하나의 값만 입력하세요.")


for i in range(len(inventory)):
    print(inventory[i])