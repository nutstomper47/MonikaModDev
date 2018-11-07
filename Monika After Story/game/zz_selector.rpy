## module that contains a workable selection screen?
#
# NOTE: i have no idea how generic this can get.
#   Chances are, it will not be very generic.
#
# Selection MAPS:
#   new class: Selec


# databaess for selectable sprite data
# currently we only store UNLOCKED
default persistent._mas_selspr_acs_db = {}
default persistent._mas_selspr_hair_db = {}
default persistent._mas_selspr_clothes_db = {}

init 200 python:

    class MASSelectableSprite(object):
        """
        Wrapper around selectable sprite objects. We do this instead of
        extending because not everything would be selectble

        PROPERTIES:
            name - this is always the same thing as the MASSprite object we
                create thsi with.
            display_name - the name to use in the selectbale button screen
            thumb - thumbnail image to use for selection screen. Aim for a
                180x180
                (png is added in the constructor)
            group - string id to group related selectable sprites. this really
                applies only to acs, but in case other things need this.
            unlocked - True if this selectable sprite can be selected, 
                False otherwise.
            visible_when_locked - True if this should be visible when locked
                False, otherwise.
                Locked items will generally be displayed with a placeholder
                thumb.
            hover_dlg - list of text to display when hovering over the object
            first_select_dlg - text to display the first time you 
                select this sprite
            select_dlg - list text to display everytime you select this sprite
                (after the first time)
            selected - True if this item is selected, False if not
        """


        def __init__(self, 
                _sprite_object,
                display_name,
                thumb, 
                group,
                visible_when_locked=True,
                hover_dlg=None,
                first_select_dlg=None,
                select_dlg=None
            ):
            """
            Selectable sprite objects constructor

            IN:
                _sprite_object - MASSpriteBase object to build this selectable
                    sprite object with.
                    NOTE: because of inheritance issues, this is NOT CHECKED.
                        The extending classes MUST check types.
                display_name - name to show on the selectable screen
                thumb - thumbnail to use on the select screen
                group - group id to group related selectable sprites.
                visible_when_locked - True if this item should be visible in
                    the screen when locked, False otherwise
                    (Default: True)
                hover_dlg - list of text to display when hovering over the 
                    object
                    (Default: None)
                first_select_dlg - text to display the first time you select
                    this sprite
                    (Default: None)
                select_dlg - list of text to display everytime you select this
                    sprite
                    (after the first time)            
                    (Default: None)
            """
#            self._check_dlg(hover_dlg)
#            self._check_dlg(first_select_dlg)
#            self._check_dlg(select_dlg)

            self.name = _sprite_object.name
            self.display_name = display_name
            self.thumb = thumb + ".png"
            self.group = group
            self.unlocked = False
            self.visible_when_locked = visible_when_locked
            self.hover_dlg = hover_dlg
            self.first_select_dlg = first_select_dlg
            self.select_dlg = select_dlg
            self.selected = False


        def _check_dlg(self, dlg):
            if dlg is not None and not renpy.has_label(dlg):
                raise Exception("label '{0}' no exist".format(dlg))


    class MASSelectableAccessory(MASSelectableSprite):
        """
        Wrapper around MASAccessory sprite objects.

        PROPERTIES:
            (no additional)

        SEE MASSelectableSprite for inherieted properties
        """

        def __init__(self,
                _sprite_object,
                display_name,
                thumb,
                group,
                visible_when_locked=True,
                hover_dlg=None,
                first_select_dlg=None,
                select_dlg=None
            ):
            """
            MASSelectableAccessory

            IN:
                _sprite_object - MASAccessory object to build this selectable
                    sprite object with.
                display_name - name to show on the selectable screen
                thumb - thumbnail to use on the select screen
                group - group id to group related selectable sprites.
                visible_when_locked - True if this item should be visible in
                    the screen when locked, False otherwise
                    (Default: True)
                hover_dlg - list of text to display when hovering over the 
                    object
                    (Default: None)
                first_select_dlg - text to display the first time you select
                    this sprite
                    (Default: None)
                select_dlg - list of text to display everytime you select this
                    sprite
                    (after the first time)            
                    (Default: None)            
            """
            if type(_sprite_object) != MASAccessory:
                raise Exception("not an acs: {0}".format(group))

            super(MASSelectableAccessory, self).__init__(
                _sprite_object,
                display_name,
                "acs-" + thumb,
                group,
                visible_when_locked,
                hover_dlg,
                first_select_dlg,
                select_dlg
            )


        def get_sprobj(self):
            """
            Gets the sprite object associated with this selectable.

            RETURNS: the sprite object for this selectbale, or None if not
                found
            """
            return store.mas_sprites.ACS_MAP.get(self.name, None)


    class MASSelectableHair(MASSelectableSprite):
        """
        Wrappare around MASHair sprite objects

        PROPERTIES:
            (no additional)

        SEE MASSelectableSprite for inherited properties
        """


        def __init__(self,
                _sprite_object,
                display_name,
                thumb,
                group,
                visible_when_locked=True,
                hover_dlg=None,
                first_select_dlg=None,
                select_dlg=None
            ):
            """
            MASSelectableHair constructor

            IN:
                _sprite_object - MASHair object to build this selectable
                    sprite object with.
                display_name - name to show on the selectable screen
                thumb - thumbnail to use on the select screen
                group - group id to group related selectable sprites.
                visible_when_locked - True if this item should be visible in
                    the screen when locked, False otherwise
                    (Default: True)
                hover_dlg - list of text to display when hovering over the 
                    object
                    (Default: None)
                first_select_dlg - text to display the first time you select
                    this sprite
                    (Default: None)
                select_dlg - list of text to display everytime you select this
                    sprite
                    (after the first time)            
                    (Default: None)            
            """
            if type(_sprite_object) != MASHair:
                raise Exception("not a hair: {0}".format(group))

            super(MASSelectableHair, self).__init__(
                _sprite_object,
                display_name,
                "hair-" + thumb,
                group,
                visible_when_locked,
                hover_dlg,
                first_select_dlg,
                select_dlg
            )


        def get_sprobj(self):
            """
            Gets the sprite object associated with this selectable.

            RETURNS: the sprite object for this selectbale, or None if not
                found
            """
            return store.mas_sprites.HAIR_MAP.get(self.name, None)


    class MASSelectableClothes(MASSelectableSprite):
        """
        Wrappare around MASClothes sprite objects

        PROPERTIES:
            (no additional)

        SEE MASSelectableSprite for inherited properties
        """


        def __init__(self,
                _sprite_object,
                display_name,
                thumb,
                group,
                visible_when_locked=True,
                hover_dlg=None,
                first_select_dlg=None,
                select_dlg=None
            ):
            """
            MASSelectableClothes constructor

            IN:
                _sprite_object - MASClothes object to build this selectable
                    sprite object with.
                display_name - name to show on the selectable screen
                thumb - thumbnail to use on the select screen
                group - group id to group related selectable sprites.
                visible_when_locked - True if this item should be visible in
                    the screen when locked, False otherwise
                    (Default: True)
                hover_dlg - list of text to display when hovering over the 
                    object
                    (Default: None)
                first_select_dlg - text to display the first time you select
                    this sprite
                    (Default: None)
                select_dlg - list of text to display everytime you select this
                    sprite
                    (after the first time)            
                    (Default: None)            
            """
            if type(_sprite_object) != MASClothes:
                raise Exception("not a clothes: {0}".format(group))

            super(MASSelectableClothes, self).__init__(
                _sprite_object,
                display_name,
                "clothes-" + thumb,
                group,
                visible_when_locked,
                hover_dlg,
                first_select_dlg,
                select_dlg
            )


        def get_sprobj(self):
            """
            Gets the sprite object associated with this selectable.

            RETURNS: the sprite object for this selectbale, or None if not
                found
            """
            return store.mas_sprites.CLOTH_MAP.get(self.name, None)


init -10 python in mas_selspr:
    import store

    # mailbox constants
    MB_DISP = "disp_text"
    MB_DISP_DEF = "def_disp_text"
    MB_CONF = "conf_enable"

    ## screen constants
    SB_VIEWPORT_BOUNDS = (1075, 5, 200, 625, 5)
    # keep this in sync with teh screen area 

    ## string constants
    DEF_DISP = "..."

    ## selection types
    SELECT_ACS = 0
    SELECT_HAIR = 1
    SELECT_CLOTH = 2

    ## selection group check
    def valid_select_type(sel_con):
        """
        Returns True if valid selection constant, False otherwise

        IN:
            sel_con - selection constnat to check

        RETURNS: True if vali dselection constant
        """
        sel_types = (SELECT_ACS, SELECT_HAIR, SELECT_CLOTH)
        return sel_con in sel_types


    ## acs/hair/clothes selection helper functions
    def is_same(old_map_view, new_map_view):
        """
        Compares the given select map views for differences.

        NOTE: we only check key existence. Use this after you clean the
        map.

        IN:
            old_map_view - viewkeys view of the old map
            new_map_view - viewkeys view of the new map

        RETURNS:
            True if the maps are the same, false if different.
        """
        old_len = len(old_map_view)

        # lengths dont match? clearly these views do not match then.
        if old_len != len(new_map_view):
            return False

        # otherwise, now we get intersection and verify length
        return old_len == len(old_map_view & new_map_view)


    # extension of mailbox
    class MASSelectableSpriteMailbox(store.MASMailbox):
        """
        SelectableSprite extension of the mailbox

        PROPERTIES:
            (no additional)

        See MASMailbox for properties.
        """

        def __init__(self, def_disp_text=DEF_DISP):
            """
            Constructor for the selectable sprite mailbox
            """
            super(MASSelectableSpriteMailbox, self).__init__()
            self.send_def_disp_text(def_disp_text)
            self.send_conf_enable(False)
        

        def _get(self, headline):
            """
            Class the super class's get

            This is just for ease of use
            """
            return super(MASSelectableSpriteMailbox, self).get(headline)


        def _send(self, headline, msg):
            """
            Calls the super classs's send

            This is just for ease of use.
            """
            super(MASSelectableSpriteMailbox, self).send(headline, msg)


        def get_conf_enable(self):
            """
            Returns the value of the conf enable message

            RETURNS:
                True if the confirmation button should be enabled, False 
                otherwise
            """
            return self._get(MB_CONF)


        def get_def_disp_text(self):
            """
            Returns the default display text message

            NOTE: does NOT remove.

            RETURNS: display text, default
            """
            return self._get(MB_DISP_DEF)


        def get_disp_text(self):
            """
            Removes and returns the display text message

            RETURNS: display text
            """
            return self._get(MB_DISP)
            

        def send_conf_enable(self, enable):
            """
            Sends enable message

            IN:
                enable - True means to enable, False means to disable 
            """
            self._send(MB_CONF, enable)


        def send_def_disp_text(self, txt):
            """
            Sends default display message

            IN:
                txt - txt to display
            """
            self._send(MB_DISP_DEF, txt)


        def send_disp_text(self, txt):
            """
            Sends display text message

            IN:
                txt - txt to display
            """
            self._send(MB_DISP, txt)


init -1 python:
    import random
    
    ## custom displayable
    class MASSelectableImageButtonDisplayable(renpy.Displayable):
        """
        Custom button for the selectable items.
        """
        import pygame
        from store.mas_selspr import MB_DISP

        # constnats
        THUMB_DIR = "mod_assets/thumb/"

        WIDTH = 180 # default width
        
        # technically this should change.
        TOTAL_HEIGHT = 218 
        SELECTOR_HEIGHT = 180 

        # this is the default, but the real may change using the expanding
        # frame properties.
        TOP_FRAME_HEIGHT = 38 # default

        # mouse stuff
        MOUSE_EVENTS = (
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP
        )
        MOUSE_WHEEL = (4, 5)

        
        def __init__(self, 
                _selectable,
                select_map,
                viewport_bounds,
                mailbox={},
                multi_select=False
            ):
            """
            Constructor for this displayable

            IN:
                selectable - the selectable object we want to encapsulate
                select_map - dict containing group keys of previously selected
                    objects.
                viewport_bounds - tuple of the following format:
                    [0]: xpos of the viewport upper left
                    [1]: ypos of the viewport upper left
                    [2]: width of the viewport
                    [3]: height of the viewport
                    [4]: border size
                mailbox - dict to send messages to outside from this
                    displayable.
                    (Default: {})
                multi_select - True means we can select more than one item.
                    False otherwise
                    (Default: False)
            """
            super(MASSelectableImageButtonDisplayable, self).__init__()

            self.selectable = _selectable
            self.select_map = select_map
            self.mailbox = mailbox
            self.multi_select = multi_select
            self.been_selected = False

            # image setups
            self.thumb = Image(self.THUMB_DIR + _selectable.thumb)
            self.thumb_overlay = Image(
                "mod_assets/frames/selector_overlay.png"
            )
            self.top_frame = Frame(
                "mod_assets/frames/selector_top_frame.png",
                left=3,
                top=3,
                tile=True
            )
            self.top_frame_selected = Frame(
                "mod_assets/frames/selector_top_frame_selected.png",
                left=3,
                top=3,
                tile=True
            )

            # renpy solids and stuff
            self.hover_overlay = Solid("#ffaa99aa")

            # text objects
            self.item_name = self._display_name(False)
            self.item_name_hover = self._display_name(True)

            # setup viewport bound values
            vpx, vpy, vpw, vph, vpb = viewport_bounds
            self.xlim_lo = vpx + vpb
            self.xlim_up = (vpx + vpw) - vpb
            self.ylim_lo = vpy + vpb
            self.ylim_up = (vpy + vph) - vpb

            # flags
            self.hovered = False
            self.hover_jumped = False # True means we just jumped to label
            self.hover_width = self.WIDTH
            self.hover_height = self.TOTAL_HEIGHT # TODO

            self.selected = False
            self.select_jump = False


        def _check_display_name(self, _display_name_text):
            """
            Checks the given display name to see if it fits within the frame
            bounds. We will have to adjust if not

            IN:
                _display_name_text - Text object of the display name

            RETURNS:
                True if it fits, False if not
            """
            return True


        def _display_name(self, selected):
            """
            Returns the text object for the display name.

            IN:
                selected - True if selected, False if not

            RETURNS:
                the text object for the display name
            """
            # TODO: auto split
            if selected:
                color = "#fa9"
            else:
                color = "#000"

            return Text(
                self.selectable.display_name,
                font=gui.default_font,
                size=gui.text_size,
                color=color,
                outlines=[]
            )


        def _hover_jump(self):
            """
            Jumps to hover if applicable.
            Also does some hover data resetting.
            """
            if self.selectable.hover_dlg is not None:
                if not self.hovered:
                    self.hover_jumped = False

                elif not self.hover_jumped:
                    self.hover_jumped = True
                    self._send_hover_text()
                    renpy.end_interaction(True)


        def _render_bottom_frame_piece(self, piece, st, at):
            """
            Renders a single bottom frame piece and returns it
            """
            return renpy.render(
                piece,
                self.WIDTH,
                self.SELECTOR_HEIGHT,
                st,
                at
            )


        def _render_bottom_frame(self, hover, st, at):
            """
            Renders the bottom frames, returns a list of the renders in order 
            of bliting.

            IN:
                hover - True means we are hovering (or are selected), false 
                    otherwise

            RETURNS:
                list of renders, in correct blit order
            """
            _renders = [
                self._render_bottom_frame_piece(self.thumb, st, at),
                self._render_bottom_frame_piece(self.thumb_overlay, st, at)
            ]

            if hover:
                _renders.append(
                    self._render_bottom_frame_piece(self.hover_overlay, st, at)
                )

            return _renders


        def _render_top_frame(self, hover, st, at):
            """
            Renders the top renders, returns a list of the renders in order of
            bliting.

            IN:
                hover - True means we are hovering (or are selected

            RETURNS:
                list of renders, in correct blit order
            """
            if hover:
                _main_piece = self._render_top_frame_piece(
                    self.top_frame_selected,
                    st,
                    at
                )

            else:
                _main_piece = self._render_top_frame_piece(
                    self.top_frame,
                    st,
                    at
                )

            return [_main_piece]


        def _render_top_frame_piece(self, piece, st, at):
            """
            Renders a top frame piece. No Text, please
            """
            # TODO smart frmae size
            return renpy.render(
                piece,
                self.WIDTH,
                self.TOP_FRAME_HEIGHT,
                st,
                at
            )


        def _render_display_name(self, hover, st, at):
            """
            Smart renders the display name. This is currently a place holder.
            """
            if hover:
                return renpy.render(
                    self.item_name_hover,
                    self.WIDTH,
                    self.TOP_FRAME_HEIGHT,
                    st,
                    at
                )

            return renpy.render(
                self.item_name,
                self.WIDTH,
                self.TOP_FRAME_HEIGHT,
                st,
                at
            )


        def _blit_bottom_frame(self, r, _renders):
            """
            bliting the bottom frames

            # TODO documentation
            """
            # TODO: modify for adjustable top frames
            for _render in _renders:
                r.blit(_render, (0, 38))


        def _blit_top_frame(self, r, _renders, _disp_name):
            """
            bliting the top frames

            # TODO documentaiton
            """
            for _render in _renders:
                r.blit(_render, (0, 0))

            # text
            # NOTE: this is top left. to do align on bottom, you must get 
            #   size
            # TODO: modify for adjustable top frames
            dnw, dnh = _disp_name.get_size()
            r.blit(_disp_name, (5, 35 - dnh))


        def _is_over_me(self, x, y):
            """
            Returns True if the given x, y is over us.
            This also handles if the mouse is past the viewport bounds.

            IN:
                x - x coord relative to upper left of this displayable
                y - y coord relative to upper left of this displayable
            """
            mouse_x, mouse_y = renpy.get_mouse_pos()
            return (
                self.xlim_lo <= mouse_x <= self.xlim_up
                and self.ylim_lo <= mouse_y <= self.ylim_up
                and 0 <= x <= self.hover_width
                and 0 <= y <= self.hover_height
            )


        def _send_msg_disp_text(self, msg):
            """
            Sends text message to mailbox.

            IN:
                msg - text message to send
            """
            self.mailbox.send_disp_text(msg)


        def _send_hover_text(self):
            """
            Sends hover text to mailbox

            ASSUMES hover text exists
            """
            self._send_msg_disp_text(
                self._rand_select_dlg(
                    self.selectable.hover_dlg
                )
            )


        def _send_first_select_text(self):
            """
            Sends first select text to mailbox

            ASSUMES first select text exists
            """
            self._send_msg_disp_text(
                self._rand_select_dlg(
                    self.selectable.first_select_dlg
                )
            )


        def _send_select_text(self):
            """
            Sends the select text to mailbox

            ASSUMES select text exists
            """
            self._send_msg_disp_text(
                self._rand_select_dlg(
                    self.selectable.select_dlg
                )
            )



        def _select(self):
            """
            Makes this item a selected item. Also handles other logic realted
            to selecting this.
            """
            # can't select self again if we are alreayd selected
            if self.selected:
                return

            # otherwise select self
            self.selected = True

            if not self.multi_select:
                # must clean select map
                for item in self.select_map.itervalues():
                    # setting to False will queue for removal of item
                    # NOTE: the caller must handle teh removal
                    item.selected = False

            # add this item to the select map
            self.select_map[self.selectable.name] = self

            if self.been_selected:
                if self.selectable.select_dlg is not None:
                    self._send_select_text()
                    renpy.end_interaction(True)

            else:
                # not been selected before
                self.been_selected = True
                if self.selectable.first_select_dlg is not None:
                    self._send_first_select_text()
                    renpy.end_interaction(True)

                elif self.selectable.select_dlg is not None:
                    self._send_select_text()
                    renpy.end_interaction(True)


        def _rand_select_dlg(self, dlg_list):
            """
            Randomly selects dialogue from the given list

            IN:
                dlg_list - list to select from

            ASSUMES the list is not empty
            """
            return dlg_list[random.randint(0, len(dlg_list)-1)]


        def event(self, ev, x, y, st):
            """
            EVENT. We only want to handle 2 cases:
                MOUSEMOTION + hover is over us
                MOUSEDOWN + mouse is over us
            """
            if ev.type in self.MOUSE_EVENTS:
                
                if ev.type == pygame.MOUSEMOTION:
                    self.hovered = self._is_over_me(x, y)
                    renpy.redraw(self, 0)

                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    
                    if ev.button in self.MOUSE_WHEEL:
                        # TODO: scrolling in mouse wheel is not perfect, 
                        #   the previously hovered item gest hovered instead
                        #   of what we actually want.
                        self.hovered = self._is_over_me(x, y)
                        renpy.redraw(self, 0)           

                    elif ev.button == 1:
                        # left click
                        self._select()
                        renpy.redraw(self, 0)

            # apply hover dialogue logic if not selected
            if not self.selected:
                self._hover_jump()



        def render(self, width, height, st, at):
            """
            Render. we want the button here.
            """
            # first, render all items.
            _bottom_renders = self._render_bottom_frame(
                self.hovered or self.selected, st, at
            )
            _top_renders = self._render_top_frame(
                self.hovered or self.selected, st, at
            )
            _disp_name = self._render_display_name(
                self.hovered or self.selected, st, at
            )

            # now blit
            r = renpy.Render(self.WIDTH, self.TOTAL_HEIGHT)
            self._blit_top_frame(r, _top_renders, _disp_name)
            self._blit_bottom_frame(r, _bottom_renders)
            return r


# now these tranforms are for the selector sidebar screen
transform mas_selector_sidebar_tr_show:
    xpos 1280 xanchor 0 ypos 10 yanchor 0
    easein 0.7 xpos 1070

transform mas_selector_sidebar_tr_hide:
    xpos 1080 xanchor 0 ypos 10 yanchor 0
    easeout 0.7 xpos 1280

style mas_selector_sidebar_vbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
#    thumb "gui/slider/horizontal_hover_thumb.png"
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    bar_vertical True
    bar_invert True

# the selector screen sidebar version should be shown, not called.
# note that we do tons of calls here, so just be ready to do tons of loop overs
# every couple of seconds.
#
# IN:
#   items - list of MASSelectableImagebuttonDisplayables to display
#   mailbox - MASSelectableSpriteMailbox for messages
#   confirm - label to jump to when confirming
#   cancel - label to jump to when canceling
screen mas_selector_sidebar(items, mailbox, confirm, cancel):
    zorder 50

    frame:
        area (1075, 5, 200, 625)
        background Frame("mod_assets/frames/black70_pinkborder100_5px.png", left=6, top=6, tile=True)

        vbox:
            xsize 200
            xalign 0.5
            viewport id "sidebar_scroll":
                mousewheel True
                arrowkeys True

                vbox:
                    xsize 200
                    spacing 10
                    null height 1

                    for selectable in items:
                        add selectable:
#                            xoffset 5
                            xalign 0.5

                    null height 1

            null height 10

            if mailbox.get_conf_enable():
                textbutton _("Confirm"):
                    style "hkb_button"
                    xalign 0.5
                    action Jump(confirm)
            else:
                ypadding 5
                xsize 120
                background Image("mod_assets/hkb_disabled_background.png")
                text "Confirm"

            textbutton _("Cancel"):
                style "hkb_button"
                xalign 0.5
                action Jump(cancel)
#                action Function(mailbox.mas_send_return, -1)

        vbar value YScrollValue("sidebar_scroll"):
            style "mas_selector_sidebar_vbar"
            xoffset -25

# GENERAL sidebar selector label
# NOTE: you should NOT call this label. You should call the helper labels
# instead.
# NOTE: this shows the `mas_selector_sidebar` screen. It is the caller's
#   responsibility to hide the screen when done.
#
# IN:
#   items - list of MASSelectable objects to select from.
#   select_type - SELECT_* constant for the current mode. We throw
#       exceptions if this is not passed in and is a valid type.
#   preview_selections - True means the selections are previewed, False means
#       they are not.
#       (Default: True)
#   only_unlocked - True means we only show unlocked items, False means
#       show everything.
#       (Default: True)
#   save_on_confirm - True means we should save selections on a confirm
#       (which means we dont undo selections), while False means we will
#       undo selections on a confirm, and let the caller handle the actual
#       selection saving.
#       (Default: True)
#   mailbox - MASSelectableSpriteMailbox object to use
#       Call send_def_disp_text to set the default display text.
#       Call send_disp_text to set the inital display text.
#       IF None, we create a MASSelectableSpriteMaibox for use.
#
# OUT:
#   select_map - map of selections. Organized like:
#       name: MASSelectableImageButtonDisplayable object
#
# RETURNS True if we are confirming the changes, False if not.
label mas_selector_sidebar_select(items, select_type, preview_selections=True, only_unlocked=True, save_on_confirm=True, mailbox=None, select_map={}):

    python:
        if not store.mas_selspr.valid_select_type(select_type):
            raise Exception(
                "invalid selection constant: {0}".format(select_type)
            )

        # otherwise, quickly setup the flags for what mode we are in.
        selecting_acs = select_type == store.mas_selspr.SELECT_ACS
        selecting_hair = select_type == store.mas_selspr.SELECT_HAIR
        selecting_clothes = select_type == store.mas_selspr.SELECT_CLOTH

        # setup the mailbox
        if mailbox is None:
            mailbox = store.mas_selspr.MASSelectableSpriteMailbox()

        # TODO unlock check
        disp_items = [
            MASSelectableImageButtonDisplayable(
                item,
                select_map,
                store.mas_selspr.SB_VIEWPORT_BOUNDS,
                mailbox
            )
            for item in items
        ]


    # TODO: this needs to be setup with speicalized types, because
    #   if we want to do previews with acs/hair/clothes, they need to be
    #   done separately.

    # TODO: need to fill the select map with what is currently selected.
    #   then that should be copied so we are aware of what is the current
    #   layout.

        if selecting_acs:
            # setup the select map for current accessories
            # that monika is wearing that are also in the item list.
            pass

        elif selecting_hair:
            # add the current hair style to the select map and mark that it
            # is selected
            for item in disp_items:
                if item.selectable.name == monika_chr.hair.name:
                    select_map[monika_chr.hair.name] = item
                    item.selected = True

        else: # selecting clothes
            # add the current clothes to the select map and mark that it is
            # selected
            for item in disp_items:
                if item.selectable.name == monika_chr.clothes.name:
                    select_map[monika_chr.clothes.name] = item
                    item.selected = True

        # make copy of old select map
        old_select_map = dict(select_map)

        # also create views that we use for comparisons
        old_view = old_select_map.viewkeys()
        new_view = select_map.viewkeys()

    show screen mas_selector_sidebar(disp_items, mailbox, "mas_selector_sidebar_select_confirm", "mas_selector_sidebar_select_cancel")

label mas_selector_sidebar_select_loop:
    python:
        # display text parsing
        disp_text = mailbox.get_disp_text()
        if disp_text is None:
            disp_text = mailbox.get_def_disp_text()

        # select map parsing
        for item in select_map.keys():
            if not select_map[item].selected:
                select_map.pop(item)
                # TODO: if preview, remove preview item.


        # once select map is cleaned, determine the confirm button enable
        mailbox.send_conf_enable(
            not store.mas_selspr.is_same(old_view, new_view)
        )

        if preview_selections:

            if selecting_acs:
                # add the accessories
        # NOTE: accessories is the caes where removal of items is very
        #   important.
                pass

            elif selecting_hair:
                for item in select_map.values():
                    if item.selected:
                        monika_chr.change_hair(item.selectable.get_sprobj())

            else: # selecting_clothes
                for item in select_map.values():
                    if item.selected:
                        monika_chr.change_clothes(item.selectable.get_sprobj())

    $ renpy.say(m, disp_text)

    jump mas_selector_sidebar_select_loop

label mas_selector_sidebar_select_confirm:
    hide screen mas_selector_sidebar
    if not save_on_confirm:
        # TODO: undo the selection map
        pass
    return True

label mas_selector_sidebar_select_cancel:
    hide screen mas_selector_sidebar
    # TODO: reset whatever to what we currently are wearing
    return False
   
# ACS sidebar selector label
#
# SEE mas_selector_sidebar_select for info on input params.
# NOTE: select_type is not a param here.
#
# RETURNS: True if we are confirming the changes, False if not
label mas_selector_sidebar_select_acs(items, preview_selections=True, only_unlocked=True, save_on_confirm=True, mailbox=None, select_map={}):

    call mas_selector_sidebar_select(items, store.mas_selspr.SELECT_ACS, preview_selections, only_unlocked, save_on_confirm, mailbox, select_map)

    return _return


# HAIR sidebar selector label
#
# SEE mas_selector_sidebar_select for info on input params.
# NOTE: select_type is not a param here.
#
# RETURNS: True if we are confirming the changes, False if not
label mas_selector_sidebar_select_hair(items, preview_selections=True, only_unlocked=True, save_on_confirm=True, mailbox=None, select_map={}):
    
    call mas_selector_sidebar_select(items, store.mas_selspr.SELECT_HAIR, preview_selections, only_unlocked, save_on_confirm, mailbox, select_map)

    return _return

# CLOTH sidebar selector label
#
# SEE mas_selector_sidebar_select for info on input params.
# NOTE: select_type is not a param here.
#
# RETURNS: True if we are confirming the changes, False if not
label mas_selector_sidebar_select_clothes(items, preview_selections=True, only_unlocked=True, save_on_confirm=True, mailbox=None, select_map={}):
    
    call mas_selector_sidebar_select(items, store.mas_selspr.SELECT_CLOTH, preview_selections, only_unlocked, save_on_confirm, mailbox, select_map)

    return _return
