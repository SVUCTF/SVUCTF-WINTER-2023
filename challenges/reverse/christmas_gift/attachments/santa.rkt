#lang racket

(define (wrap-gift gift)
  (define (merry-coding index len)
    (when (< index len)
      (let* ([char-code (char->integer (string-ref gift index))]
             [encoded-char (cond [(and (>= char-code 97) (<= char-code 122)) (- char-code 32)]
                                 [(and (>= char-code 65) (<= char-code 90)) (+ char-code 32)]
                                 [else char-code])]
             [encoded-char (bitwise-xor index encoded-char)])
        (printf "#~a" encoded-char)
        (merry-coding (+ index 1) len))))
  (merry-coding 0 (string-length gift))
  (newline))

(define (christmas-greetings)
  (let ([gift "flag{???????????????????????????}"])
    (wrap-gift gift)))

(christmas-greetings)
