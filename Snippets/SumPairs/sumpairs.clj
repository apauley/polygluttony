; Solution by Timothy Pratley
; http://groups.google.com/group/clojure/browse_thread/thread/ca3ad049fba7ee82

(def a '(1 2 3 4 5))
(map + a (rest a))
