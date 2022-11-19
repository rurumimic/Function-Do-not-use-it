;; clj -M example.clj

(ns hof.example)

(->> (range) ;; (0 1 2 3 4 5 6 ...)
     (map inc) ;; (1 2 3 4 5 6 7 ...)
     (filter even?) ;; (2 4 6 8 10 12 14 ...)
     (take 5) ;; (2 4 6 8 10)
     (reduce +) ;; => 30
     (println))
