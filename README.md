# Transformer Ve Sağlıkta Yapay Zeka 

Bu çalışmada Dopler sound datalarından embolik sinyallerin yapay zeka ile ortaya çıkarılması üzerine kurgulanan bir fikir üzerine bir denemedir.
Transformer kodlarının buradaki amacı dopler sinyallerinden özellik çıkarımı yapmak için kullanımak üzere seçilen bir mimaridir. Bu mimariyi 
trercih edilmesindeki en büyük neden chat-gpt deki başarılarından dolayıdır. Ancak burada kullanması planlanan sadece transformerin encoder kısmı 
olarak düşünülmüşür. Ve böylelikle dopler sound için bir özellik çıkarımında bulanabilecektik. Fakat elimizdeki dataların boyut farkından kaynaklanan 
bir problemden dolayı istediğimiz sonucu elde edilemedi. 

Buradaki kodlar çalışmanın gerçekleşbiliritesi için bir deneme yanılma olarak kullanılmak için hazır kodlardan yararlanılmıştır.
Bu kodların sahibi youtube daki www.youtube.com/@CodeEmporium kanalından alınmıştır.
Her kode aşağıdaki vide da daha ayrıntılı bahsedilmiştir 

- Self Attention in Transformer Neural Networks -> https://youtu.be/QCJQG4DuHT0
- Multi Head Attention in Transformer Neural Networks -> https://youtu.be/HQn1QKQYXVg 
- Positional Encoding in Transformer Neural Networks -> https://youtu.be/ZMxVe-HK174
- Layer Normalization -> https://youtu.be/G45TuC6zRf4
- Blowing up the Transformer -> https://youtu.be/QwfuoNhjbkI 
- Transformer Encoder in 100 lines of code! -> https://youtu.be/g3sEsBGkLU0

Bu video seirisinin devamında transformerın decoder kısmıda bahsedilmektedir. 
Biz bu projede bu adıma kadar planladık ve başarısız olduk bunun sonucunda transformer mimarisinin encoding kısmında bitirdik.

Dopler sounda datalarından özellik çıkartmak için Transformer yerine Short Time Fourier Transform kullanarak spectogram elde edilemsi planlanmaktadır.
Diğer bir resporiteris de paylaşacağım. 










