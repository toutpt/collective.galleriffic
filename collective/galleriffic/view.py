from zope import component
from zope import schema
from zope import interface
from zope.i18nmessageid import MessageFactory
from zope.i18n import translate
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.configviews import ConfigurableBaseView

_ = MessageFactory('collective.galleriffic')

class IGallerifficConfiguration(interface.Interface):
    """Galleriffic options"""
    
    delay = schema.Int(title=_(u"Delay"),
                       description=_(u"in milliseconds"),
                       default=3000)
    
    numThumbs = schema.Int(title=_(u"Number of thubnails to show per page"),
                           default=20)
    
    preloadAhead = schema.Int(title=_(u"Preload"),
                              description=_(u"Set to -1 to preload all images"),
                              default=40)

    enableTopPager = schema.Bool(title=_(u"Enable top pager"),
                                 default=False)
    
    enableBottomPager = schema.Bool(title=_(u"Enable bottom pager"),
                                    default=True)
    
    maxPagesToShow = schema.Int(title=_(u"Max pages to show"),
                                description=_(u"The maximum number of pages to display in either the top or bottom pager"),
                                default=7)
    
    renderSSControls = schema.Bool(title=_(u"Render SS controls"),
                                   description=_(u"Specifies whether the slideshow's Play and Pause links should be rendered"),
                                   default=True)
    
    renderNavControls = schema.Bool(title=_(u"Render navigation controls"),
                                   description=_(u"Specifies whether the slideshow's Next and Previous links should be rendered"),
                                   default=True)
    
    enableHistory = schema.Bool(title=_(u"Enable history"),
                                description=_(u"Specifies whether the url's hash and the browser's history cache should update when the current slideshow image changes"),
                                default=False)
    
    enableKeyboardNavigation = schema.Bool(title=_(u"Enable Keyboard navigation"),
                                           description=_(u"Specifies whether keyboard navigation is enabled"),
                                           default=True)
    
    autoStart = schema.Bool(title=_(u"Autostart"),
                            description=_(u"Specifies whether the slideshow should be playing or paused when the page first loads"),
                            default=False)
    
    syncTransitions = schema.Bool(title=_(u"Sync transitions"),
                                  description=_(u"Specifies whether the out and in transitions occur simultaneously or distinctly"),
                                  default=False)
    
    defaultTransitionDuration = schema.Int(title=_(u"default transition duration"),
                                           description=_(u"If using the default transitions, specifies the duration of the transitions"),
                                           default=1000)

class GallerifficView(ConfigurableBaseView):
    """Galleriffic configurable view"""
    settings_schema = IGallerifficConfiguration
    jsvarname = 'galleriffic_config'
    settings_providers = ('context.zope.annotation',)

    display_mode_1 = ViewPageTemplateFile('display_mode_1.pt')
    display_mode_2 = ViewPageTemplateFile('display_mode_2.pt')
    display_mode_3 = ViewPageTemplateFile('display_mode_3.pt')
    display_mode = 'display_mode_1'

    def __call__(self):
        dm = self.display_mode
        view = getattr(self, dm, None)
        if view is None:
            view = self.display_mode_1
        return view()

    def stylesheet(self):
        dm = self.display_mode
        css = '/++resource++galleriffic/%s.css'%dm
        portal_state = component.getMultiAdapter((self.context, self.request), 
                                                 name=u'plone_portal_state')
        portal_url = portal_state.portal_url()
        return portal_url + css

    @property
    def settings(self):
        settings = super(GallerifficView, self).settings
        lang = self.language()

        def t(msgid):
            return translate(msgid, domain="collective.galleriffic",
                     context=self.context, target_language=lang)

        settings['playLinkText'] =  t(_(u"Play"))
        settings['pauseLinkText'] = t(_(u"Pause"))
        settings['prevLinkText'] =  t(_(u"Previous"))
        settings['nextLinkText'] =  t(_(u"Next"))
        settings['nextPageLinkText'] = t(_(u"Next &raquo;"))
        settings['prevPageLinkText'] = t(_(u"&laquo; Prev"))

        return settings

    def language(self):
        """
        @return: Two letter string, the active language code
        """
        portal_state = component.getMultiAdapter((self.context, self.request),
                                                 name=u'plone_portal_state')
        current_language = portal_state.language()
        return current_language

