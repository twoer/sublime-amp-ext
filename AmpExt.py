import sublime, sublime_plugin

setting = sublime.load_settings("amp-data.sublime-settings")
data = setting.get('data')

class AmpExtCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_quick_panel(data, self.panel_done)

	def panel_done(self, picked):
		if(picked <0):
			return
		edit = self.view.begin_edit()
		begin  = self.view.sel()[0].begin()
		selLen = len(self.view.substr(self.view.sel()[0]))
		if(selLen <= 0):
			self.view.insert(edit, self.view.sel()[0].begin(),data[picked][0])
		else:
			self.view.replace(edit, sublime.Region(begin,begin + selLen),data[picked][0])
	