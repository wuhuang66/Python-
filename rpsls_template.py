#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�̷С��
���ڣ�2021/11/26
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name =="ʯͷ":
        return 0

    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error: No Correct Name")
# input("����")
    # """
    # ����Ϸ�����Ӧ����ͬ������
    # """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


   #pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    if number in range(0,5):
        if number==0:
            return "ʯͷ"
        elif number==1:
            return "ʷ����"
        elif number==2:
            return "ֽ"
        elif number==3:
            return "����"
        elif number==4:
            return "����"
        else:
            print("Error input")

  #  ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
   # pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    print("-------- ")
    player_number=name_to_number(player_choice)#���û������ѡ��תΪ����
    comp_number=random.randrange(0,5)#���������
    comp_choice=number_to_name(comp_number)#�������������������תΪѡ��
    print("�������ѡ��Ϊ��"+str(comp_choice))
    if player_number - comp_number in range(-4,-2):
        print("��Ӯ��!")
    elif player_number - comp_number in range(1, 3):
        print("��Ӯ��!")
    elif player_number - comp_number in range(-2,0):
        print("������!")
    elif player_number - comp_number in range(3,5):
        print("������!")
    elif player_number - comp_number==0:
        print("���ͼ����ѡ���һ��")
    else:
        print("error!")    # """
    # �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    #
    # """
    #

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    # pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
#
#
