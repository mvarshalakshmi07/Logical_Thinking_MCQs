score = 0

questions = [
    {
        "question": "1.Five people A, B, C, D, and E are sitting in a row facing north. A is to the right of B but to the left of C. D is at the extreme left. Who is at the extreme right?",
        "options": ["(A) A     (B) B     (C) C     (D) E"],
        "answer": "C"
    },
    {
        "question": "2.Seven persons P, Q, R, S, T, U, and V are standing in a line. Q is between P and R. S is to the immediate left of T. V is at one end. Who is second from the left?",
        "options": ["A) P       B) Q      C) S      D) Cannot be determined"],
        "answer": "D"
    },
    {
        "question": "3. A, B, C, D, E are seated in a row. C is not next to A. D is at one end. A is next to B. Who is in the middle?",
        "options": ["A) A      B) B       C) C      D) E"],
        "answer": "C"
    },
    {
        "question": "4. Six boys are standing in a line. A is taller than B but shorter than C. D is taller than E but shorter than F. Who is the tallest?",
        "options": ["A) C    B) F    C) A    D) Cannot be determined"],
        "answer": "D"
    },
    {
        "question": "5. Eight people sit in a row. M is third from left, N is fourth from right. How many people are between M and N?",
        "options": ["A) 1    B) 2    C) 3    D) 4"],
        "answer": "B"
    },
    {
        "question": "6. Eight people are sitting in a circle facing the center. A is second to the left of B. C is opposite A. Who is opposite B?",
        "options": ["(A) A     (B) C      (C) D      (D) Cannot be determined"],
        "answer": "D"
    },
    {
        "question": "7. Six persons are sitting around a circular table. P is between Q and R. S is opposite P. Who is opposite Q?",
        "options": ["A) R     B) S      C) None of the above      D) P"],
        "answer": "C"
    },
    {
        "question": "8. Five friends are sitting in a circle facing outward. A is to the immediate right of B. C is between D and E. Who is to the left of A?",
        "options": ["A) B    B) C       C) D         D) Cannot be determined"],
        "answer": "B"
    },
    {
        "question": "9.Eight persons sit in a circle. A is opposite C. B is between A and D. Who is opposite B?",
        "options": ["A) C    B) D       C) A         D) Cannot be determined"],
        "answer": "D"
    },
    {
        "question": "10. Seven people sit around a circular table. P is third to the left of Q. R is opposite Q. Who is second to the right of R?",
        "options": ["A) P   B) Q        C) S         D) None of the above"],
        "answer": "D"
    },
    {
        "question": "11. Five people P, Q, R, S, T live on floors 1 to 5. P lives above Q but below R. S lives on topmost floor. Who lives on the first floor?",
        "options": ["A) Q        B) P       C) R         D) T"],
        "answer": "D"
    },
    {
        "question": "12. Three girls A, B, C like different fruits: 🍎, 🍌, 🍊. A does not like 🍎. B likes 🍌. Who likes 🍊?",
        "options": ["A) B        B) A       C) C          D) Cannot be determined"],
        "answer": "A"
    },
    {
        "question": "13. Four friends live in different houses (Red, Blue, Green, Yellow). P lives in Red. Q does not live in Blue or Green. R lives in Yellow. Who lives in Blue?",
        "options": ["A) P        B) Q       C) R          D) Cannot be determined"],
        "answer": "A"
    },
    {
        "question": "14. Five students rank differently in Maths. A is better than B but worse than C. D is worse than E. Who is the best?",
        "options": ["A) C        B) E       C) A         D) Cannot be determined"],
        "answer": "B"
    },
    {
        "question": "15. Four persons A, B, C, and D are sitting on four chairs in a row facing north. Each wears a different color: Red, Blue, Green, Yellow."
                    "A sits second from the left and wears Red."
                    "B sits to the immediate right of A and wears Blue."
                    "C sits at the extreme right."
                    "Who wears Green? ",
        "options": ["A) A         B) None of the Above    C) Can not determine      D) D"],
        "answer": "D"
    },
    {
        "question": "16. Pointing to a girl, Ram said, “She is the daughter of my father’s only son.” Who is the girl?",
        "options": ["A) Sister      B) Cousin     C) Niece     D) Daughter"],
        "answer": "B"
    },
    {
        "question": "17. A is the brother of B. B is the mother of C. How is A related to C?",
        "options": ["A) Uncle      B) Father     C) Brother  D) Grandfather"],
        "answer": "A"
    },
    {
        "question": "18. Introducing a man, a woman said, “His wife is the only daughter of my father.” How is the man related to the woman?",
        "options": ["A) Brother    B) Son-in-law        C) Husband               D) Brother-in-law"],
        "answer": "C"
    },
    {
        "question": "19. P is the son of Q. Q is the brother of R. How is R related to P?",
        "options": ["A) Aunt      B) Uncle              C) Mother            D) Grandmother"],
        "answer": "B"
    },
    {
        "question": "20. X is the sister of Y. Y is the son of Z. How is Z related to X?",
        "options": ["A) Father   B) Mother              C) Parent            D) Cannot be determined"],
        "answer": "C"
    },
]

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct ✅")
        score += 5
    else:
        print("Wrong ❌")
        score -= 1
print("Your Final Score:", score)
