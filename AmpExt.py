import sublime, sublime_plugin

setting = sublime.load_settings("amp_data.sublime-settings")
data = setting.get('data')

class AmpExtCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_quick_panel(data, self.panel_done)

	def panel_done(self, picked):
		edit = self.view.begin_edit()
		self.view.insert(edit, self.view.sel()[0].begin(),data[picked][0])
	