import os
if os.path.isfile('output.txt'):
    print('歡迎使用中日對照小工具')
    with open('output.txt', 'r',encoding = 'utf-8') as f:
        result = {}
        for line in f.readlines():
            line = line.strip()
            if not len(line):
                continue
            result[line.split(':')[0]] = line.split(':')[1]
else:
    print('"output.txt"檔案不在資料夾中，請放置於相同資料夾內')

KC_dic = result
print('************************')
print('請輸入日文字。或按q退出')
print('************************')

while True:
  #print('Enter a JP word or enter q to quit')
  #print('==========================')
  #print('歡迎使用中日對照小工具，請輸入日文字。或按q退出')
  #print('==========================')
  JP_word = input()
  if JP_word == 'q':
    print('請關視窗並檢視"output.txt"查看')
    break

  if JP_word in KC_dic:
    #for key,value in KC_dic.items():
    print('************************')
    print('查詢結果: 對應的中文字義為[' + KC_dic[JP_word] + ']')
    print('************************')
    print('繼續使用時，請輸入日文字。或按q退出')
  else:
    print(JP_word+' 這個字還沒對應的中文，請輸入適當的中文')
    CH_word = input()
    KC_dic[JP_word] = CH_word
    KC_dic.update({JP_word:CH_word})
    print('中文已被更新')
    print('繼續使用時，請輸入日文。或按q退出')

  #print('==========================')
  #print('目前中日對照的資料有: ')
  #print(KC_dic)
  #print('請按q退出查看檔案"output.txt"確認')
  #print('==========================')

with open('output.txt','w', encoding='utf-8') as fout:
    for k, v in KC_dic.items():
        dic = k +':'+ v + '\n'
            #print(dic)
        fout.write(dic)
    print(fout)
