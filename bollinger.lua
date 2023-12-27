instrument { name = "ATR & Bollinger", overlay = true }

period = input (13, "front.period", input.integer, 1   )
shift  = input (3, "front.newind.offset", input.double, 1   )

source = input (1, "front.ind.source", input.string_selection, inputs.titles_overlay)
local sourceSeries = inputs [source]

atr = rma (tr, period)

h = sourceSeries + atr * shift
l = sourceSeries - atr * shift

-- bollinger

period1 = input (20,"front.period", input.integer,  1)
devs   = input (2, "front.newind.stddev", input.integer, 1)
fn     = input (1, "front.newind.average", input.string_selection, averages.titles)

local sourceSeries = inputs [source]
local averageFunction = averages [fn]

middle = averageFunction (sourceSeries, period1)
scaled_dev = devs * stdev (sourceSeries, period1)

top = middle + scaled_dev
bottom = middle - scaled_dev

end

plot (top, "front.top line", top_color, top_width)
plot (middle, "front.middle line", middle_color, middle_width)
plot (bottom, "front.bottom line", bottom_color, bottom_width)