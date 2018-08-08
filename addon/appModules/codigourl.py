def script_url(self, gesture):
		if not self.inMainWindow():
			ui.message(_("Not available here"))
			return
        path = (("id", "nav-bar"), ("id", "urlbar"), ("id", "identity-box",))
        secInfoButton = self.searchObject(path)
        if secInfoButton:
            securInfo = secInfoButton.description # This has changed in FF 57. Keeping this line for compatibility with earlier versions.
            try: # This one is for FF 57 and later.
                securInfo = secInfoButton.firstChild.next.name if secInfoButton.firstChild.next.IA2Attributes["id"] == "connection-icon" else ""
                if securInfo:
                    owner = " ".join([o.name for o in filter(lambda o: o.role == controlTypes.ROLE_STATICTEXT, secInfoButton.recursiveDescendants)])
                    securInfo = "%s, %s" % (owner, securInfo) if owner else securInfo
            except:
                pass
            #TRANSLATORS: this connection is using http, not https
            securInfo  = _("Insecure connection") if not securInfo   else securInfo  
            url = secInfoButton.next.value
            ui.message("%s (%s)" % (url, securInfo))
            if scriptHandler.getLastScriptRepeatCount() == 1:
                if api.copyToClip(url):
                    #TRANSLATORS: message spoken when an item hast just been copied to the clipboard
                    ui.message(_("Copied to clipboard"))
            return
        #TRANSLATORS: message spoken when addres bar could not be found
        ui.message (_("Address not found"))
    
	def searchObject(self, path):
		obj = api.getForegroundObject()
        for milestone in path:
            obj = self.searchAmongTheChildren(milestone, obj)
            if not obj:
                return
        return obj

	def searchAmongTheChildren(self, id, into):
		if not into:
			return(None)
        key, value = id
        obj = into.firstChild
        if key in obj.IA2Attributes.keys():
            if obj.IA2Attributes[key] == value:
                return(obj)
        while obj:
            if key in obj.IA2Attributes.keys():
                if obj.IA2Attributes[key] == value:
                    break
            obj = obj.next
        return(obj)

	def inMainWindow(self):
		try:
			if api.getForegroundObject().IA2Attributes["id"] != "main-window":
				return False
		except (AttributeError, KeyError):
			return False
        return True		