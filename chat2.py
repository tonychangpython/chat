# 讀取對話紀錄
def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#文字計數			
def wound_convert(lines):
	wc = {}
	for d in lines:
		lines = d.split()
		for line in lines:
			if line in wc:
				wc[line] += 1
			else:
				wc[line] = 1 #新增新的key進wc字典
	for line in wc:
		if wc[line] > 50:
			print(line, wc[line])
	return wc					
	print(len(wc))

def search_word(wc):
	while True:
		line = input('請問你想查什麼字: ')
		if line =='q':
			break
		if line in wc:
			print(line, '出現過的次數為', wc[line])
		else:
			print('這個字沒出現過喔')
			print('感謝查詢')

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('FB2.txt')
	wc = wound_convert(lines)
	search_word(wc)
	# write_file('output.txt', lines)
main()	