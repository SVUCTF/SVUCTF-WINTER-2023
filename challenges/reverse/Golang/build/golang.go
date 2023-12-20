package main

import (
	"bytes"
	"encoding/base64"
	"fmt"
)

func main() {
	var input []byte
	encodedFlag := []byte("wrY7w=/gEoSF3m7VEr31frPbuxLR3m7VEr3P")

	fmt.Print("input: ")
	fmt.Scan(&input)

	customEncoding := base64.NewEncoding("HNO4klm6ij9n+J2hyf0gzA8uvwDEq3X1Q7ZKeFrWcVTts/MRGYbdxSo=ILaUpPBC")
	customEncoding = customEncoding.WithPadding('5')

	encodedInput := make([]byte, customEncoding.EncodedLen(len(input)))
	customEncoding.Encode(encodedInput, input)

	if bytes.Equal(encodedInput, encodedFlag) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
