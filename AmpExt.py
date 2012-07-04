import sublime, sublime_plugin

setting = sublime.load_settings("amp_data.sublime-settings")

class AmpExtCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		list = setting.get('list')
		self.view.window().show_quick_panel(list, self.panel_done)

	def panel_done(self, picked):
		if 0 > picked < len(amp_data):
			return
		edit = self.view.begin_edit()
		self.view.insert(edit, self.view.sel()[0].begin(),amp_data[picked][0])
	