import webapp2

routes = [
	webapp2.Route('/'                   , handler='home.Home'           , name='home'),
	webapp2.Route('/add'                , handler='add.Add'             , name='add'),
	webapp2.Route('/add/error'          , handler='add.AddError'        , name='add_error'),
	webapp2.Route('/upload/images/(.+)' , handler='upload.UploadImages' , name='upload_images'),
	webapp2.Route('/upload/handler/(.+)', handler='upload.UploadHandler', name='upload_handler')
]

config = {
	'webapp2_extras.sessions': 	{
    	'secret_key': 'ru#qgro%ta=lc*wohb%)rqg*^)x6hn=tr)2@&amp;4d^&amp;j%i$sae)@'
	}
}

debug = True