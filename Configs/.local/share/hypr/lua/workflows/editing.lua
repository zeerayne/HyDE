local workflow = {
  name = "Editing",
  icon = "",
  description = "Best for writing and editing // Disables xray and blur that might affect color picking/contrast",
}

if not hl then
  return workflow
end

hl.config({
  decoration = {
    active_opacity = 1,
    inactive_opacity = 1,
    fullscreen_opacity = 1,
  },
})
