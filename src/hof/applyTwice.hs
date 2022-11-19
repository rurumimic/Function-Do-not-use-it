-- stack ghci
-- :l applyTwice.hs
--
-- [1 of 1] Compiling Main             ( applyTwice.hs, interpreted )
-- Ok, one module loaded.

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

-- applyTwice (+3) 10
-- 16

-- applyTwice (++ " HAHA") "HEY"
-- "HEY HAHA HAHA"

-- applyTwice ("HAHA " ++) "HEY"
-- "HAHA HAHA HEY"

-- applyTwice (3:) [1]
-- [3,3,1]

-- :quit
-- Leaving GHCi.