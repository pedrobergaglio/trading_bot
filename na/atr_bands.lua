instrument { name = "ATR & Bollinger Bands", overlay = true, icon="indicators:ATR" }

period = input (13, "front.period", input.integer, 1   )
shift  = input (3, "front.newind.offset", input.double, 1   )

source = input (1, "front.ind.source", input.string_selection, inputs.titles_overlay)

input_group {
    "front.newind.lines",
    color = input { default = rgba(75,255,181,0.7), type = input.color },
    width = input { default = 1, type = input.line_width}
}

input_group {
    "front.newind.adx.fill",
    fill_color = input { default = rgba(75,255,181,0.1), type = input.color },
    fill_visible = input { default = true, type = input.plot_visibility }
}

local sourceSeries = inputs [source]

atr = rma (tr, period)

h = sourceSeries + atr * shift
l = sourceSeries - atr * shift

--if fill_visible then
--    fill (l, h, "", fill_color)

--plot (h, "", color, width)
--plot (l, "", color, width)


-- bollinger

--instrument { name = "Bollinger Bands", overlay = true, icon = "indicators:BB" }

period1 = input (20,"front.period1", input.integer,  1)
devs1   = input (2, "front.newind.stddev", input.integer, 1)
source1 = input (1, "front.ind.source1", input.string_selection, inputs.titles_overlay)
fn1     = input (1, "front.newind.average", input.string_selection, averages.titles)

input_group {
    "front.top1 line",
    top1_color = input { default = "#4BFFB5", type = input.color },
    top1_width = input { default = 1, type = input.line_width}
}

input_group {
    "front.middle1 line",
    middle1_color = input { default = "#FF6C58", type = input.color },
    middle1_width = input { default = 1, type = input.line_width}
}

input_group {
    "front.bottom1 line",
    bottom1_color = input { default = "#4BFFB5", type = input.color },
    bottom1_width = input { default = 1, type = input.line_width}
}

input_group {
    "front.newind.adx.fill",
    fill_color = input { default = rgba(75,255,181,0.08), type = input.color },
    fill_visible = input { default = true, type = input.plot_visibility}
}

local sourceSeries1 = inputs [source1]
local averageFunction1 = averages [fn1]

middle1 = averageFunction1 (sourceSeries1, period1)
scaled_dev1 = devs1 * stdev1 (sourceSeries1, period1)

top1 = middle1 + scaled_dev1
bottom1 = middle1 - scaled_dev1

if fill_visible then
    fill (bottom1, top1, "", fill_color)
end

plot (top1, "front.top1 line", top1_color, top1_width)
plot (middle1, "front.middle1 line", middle1_color, middle1_width)
plot (bottom1, "front.bottom1 line", bottom1_color, bottom1_width)