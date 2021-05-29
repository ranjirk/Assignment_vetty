import flask, codecs
from flask import request
app = flask.Flask(__name__)

class render_file:
	def center(self, file, start, end):
		self.filename, self.start_line, self.end_line = file, start, end
		if self.start_line == "-1" and self.end_line == "-1" :
			self.ret_content = self.full_file(self.filename)
		elif self.start_line == "0" or self.end_line == "0":
			self.ret_content = "|Start / End line cannot be zero|"
		else :
			self.ret_content = self.part_file(self.filename, self.start_line, self.end_line)
		return self.ret_content if self.ret_content else "No content returned, internal error"

	def full_file(self, file):
		self.file, self.data1 = file, []
		self.f1 = codecs.open(self.file, 'r+', encoding='utf-16')
		self.data1 = self.f1.read()
		self.f1.close()
		# self.ff = codecs.open('result.txt', 'w', encoding='utf-16')
		# self.ff.write(self.data1)
		# self.ff.close()
		return self.data1 if self.data1 else False

	def part_file(self, file, start, end):
		self.name_, self.start_, self.end_ = file, int(start), int(end)
		self.f2 = codecs.open(self.name_,'r+',encoding='utf-16')
		self.content2 = self.f2.read()
		self.f2.close()
		self.occ = [self.i for self.i, self.ele in enumerate(self.content2) if self.ele == '\n']
		self.data2 = self.content2[self.occ[self.start_-2]+1:self.occ[self.end_-1]]
		# self.f3 = codecs.open('result.txt', 'w', encoding='utf-16')
		# self.f3.write(self.data2)
		# self.f3.close()
		return self.data2 if self.data2 else False

@app.route('/hello')
def hello():
	file_name = request.args.get('name', default = "file1.txt", type = str)
	start_line = request.args.get('start', default = '-1', type = str)
	end_line = request.args.get('end', default = '-1', type = str) 
	obj = render_file()
	result = obj.center(file_name, start_line, end_line)
	return flask.render_template_string(result)
app.run(debug=True, host="0.0.0.0", port=8000)
