import webapp2

routes = [
	webapp2.Route('/'                              , handler='home.Home'           , name='home'),
	webapp2.Route('/about'                         , handler='about.About'         , name='about'),
	webapp2.Route('/add'                           , handler='add.Add'             , name='add'),
	webapp2.Route('/add/error'                     , handler='add.AddError'        , name='add_error'),
	webapp2.Route('/dagkots/get'                   , handler='home.Dagkots'        , name='dagkots_get'),
	webapp2.Route('/upload/images/<dagkot_key:.+>' , handler='upload.UploadImages' , name='upload_images'),
	webapp2.Route('/upload/handler/<dagkot_key:.+>', handler='upload.UploadHandler', name='upload_handler'),
	webapp2.Route('/view/<dagkot_key:.+>'          , handler='dagkot.View'         , name='view')
]

config = {
	'webapp2_extras.sessions': 	{
    	'secret_key': 'ru#qgro%ta=lc*wohb%)rqg*^)x6hn=tr)2@&amp;4d^&amp;j%i$sae)@'
	}
}

debug = True

DAGKOTS_PER_PAGE = 10