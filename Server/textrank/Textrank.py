from konlpy.tag import Kkma
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy

class SentenceTokenizer(object):
    def __init__(self):
        self.kkma = Kkma()
        self.okt = Okt()
        self.stopwords = ['아', '야', '휴', '나', '우리', '저', '저희', '을', '를', '의', '에', '가',]

    def text2sentences(self, text):
        sentences = self.kkma.sentences(text)
        for idx in range(0, len(sentences)):
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        return sentences

    def get_nouns(self, sentences):
        nouns = []
        for sentence in sentences:
            if sentence is not '':
                nouns.append(' '.join([noun for noun in self.okt.nouns(str(sentence))if noun not in self.stopwords and len(noun) > 1]))
        return nouns

class GraphMatrix(object):
    def __init__(self):
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        self.graph_sentence = []

    def build_sent_graph(self, sentence):
        tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
        self.graph_sentence = numpy.dot(tfidf_mat, tfidf_mat.T)
        return self.graph_sentence

    def build_words_graph(self, sentence):
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
        vocab = self.cnt_vec.vocabulary_
        return numpy.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}

class Rank(object):
    def get_ranks(self, graph, d=0.85):
        A = graph
        matrix_size = A.shape[0]
        for id in range(matrix_size):
            A[id, id] = 0
            link_sum = numpy.sum(A[:,id])
            if link_sum != 0:
                    A[:, id] /= link_sum
            A[:, id] *= -d
            A[id, id] = 1
        B = (1-d) * numpy.ones((matrix_size, 1))
        ranks = numpy.linalg.solve(A, B) # 연립방정식 Ax = B
        return {idx: r[0] for idx, r in enumerate(ranks)}

class TextRank(object):
    def __init__(self, text):
        self.sent_tokenize = SentenceTokenizer()
        self.sentences = self.sent_tokenize.text2sentences(text)
        self.nouns = self.sent_tokenize.get_nouns(self.sentences)
        self.graph_matrix = GraphMatrix()
        self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns)
        self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns)
        self.rank = Rank()
        self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
        self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True) # 문장 정렬

    def summarize(self, sent_num=5):
        summary = []
        index=[]
        for idx in self.sorted_sent_rank_idx[:sent_num]:
            index.append(idx)
        index.sort()
        for idx in index:
            summary.append(self.sentences[idx])
        return summary

    def keywords(self, word_num=10):
        rank = Rank()
        rank_idx = rank.get_ranks(self.words_graph)
        sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)
        keywords = []
        index=[]
        for idx in sorted_rank_idx[:word_num]:
            index.append(idx)
        for idx in index:
            keywords.append(self.idx2word[idx])
        return keywords

path = "F:/AIVIS/Git Workspace" # 자신의 git directory
fData = open(path+'/aivis/Server/textrank/data.txt', 'r', encoding='UTF-8')
fSummarize = open(path+'/aivis/Server/textrank/summarize.txt', 'w', encoding='UTF-8')
fKeywords = open(path+'/aivis/Server/textrank/keywords.txt', 'w', encoding='UTF-8')

data = fData.read()
textrank = TextRank(data)

#print('Summarize:')
for row in textrank.summarize():
    #print(row)
    fSummarize.write(row)
    fSummarize.write('\n')
#print()

#print('Keywords:')
for keyword in textrank.keywords():
    #print(keyword)
    fKeywords.write(keyword)
    fKeywords.write('\n')
#print()

fData.close()
fSummarize.close()
fKeywords.close()
