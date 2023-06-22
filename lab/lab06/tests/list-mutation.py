test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          Nothing
          >>> lst
          [5, 6, 7, 8, 6]
          >>> lst.insert(0, 9)
          >>> lst
          [9, 5, 6, 7, 8, 6]
          >>> x = lst.pop(2)
          >>> lst
          [9, 5, 7, 8, 6]
          >>> lst.remove(x)
          >>> lst
          9a5a83015493c89b42df02f7bc04f9f8
          # locked
          >>> a, b = lst, lst[:]
          >>> a is lst
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> b == lst
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> b is lst
          a559f517e8f86de30b928d7e29ec2331
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
