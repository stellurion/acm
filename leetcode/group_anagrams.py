
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #freq
        freq = []
        for s in strs:
            mapping = defaultdict(lambda: 0)
            for chara in s:
                mapping[chara] += 1
            freq.append(mapping)

        result = []
        seen = set()

        for s in range(len(strs)):
            if not strs[s] in seen:
                indexes = [x for x in range(len(freq)) if freq[x] == freq[s]]
                
                group = []
                for i in indexes:
                    group.append(strs[i])
                    seen.add(strs[i])
                result.append(group)

        return result

                