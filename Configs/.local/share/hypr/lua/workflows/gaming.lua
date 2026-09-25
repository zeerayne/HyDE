local workflow = {
  name = "Gaming",
  icon = "",
  description = "Emphasis on performance and disabling compositors expensive features",
}

if not hl then
  return workflow
end

hl.config({
  general = {
    gaps_in = 0,
    gaps_out = 0,
    border_size = 1,
  },
  decoration = {
    shadow = {
      enabled = false,
    },
    blur = {
      enabled = false,
    },
    rounding = 0,
    active_opacity = 1,
    inactive_opacity = 1,
    fullscreen_opacity = 1,
  },
  animations = {
    enabled = false,
  },
})
