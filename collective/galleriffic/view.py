from zope import schema
from zope import interface
from zope.i18nmessageid import MessageFactory

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
    
