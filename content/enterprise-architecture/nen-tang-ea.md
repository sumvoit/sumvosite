---
title: "Nền tảng Enterprise Architecture (EA)"
weight: 11
---

# Enterprise Architecture — Kiến trúc Doanh nghiệp

Toàn bộ 73 slide của khóa _“Enterprise Architecture: Introduction & Example”_ được hệ thống hóa theo 3 module, mỗi slide có mô tả, diễn giải chi tiết, ví dụ, câu hỏi thường gặp và mạch nối. Dùng 3 lăng kính bên dưới để lọc nội dung theo vai trò của một kiến trúc sư doanh nghiệp.

**Chiến lược** → Hiện trạng · **Baseline** → Khoảng cách · **Gap** → Mục tiêu · **Target** → Lộ trình · **Roadmap** → **Giá trị**

Nguồn: slide bài giảng EA v2026.1 · Tham chiếu chuẩn [TOGAF 10 — The Open Group](https://digital-portfolio.opengroup.org/togaf-standard/latest/home-page.html)

Ba lăng kính — Ba chiếc mũ của Kiến trúc sư Doanh nghiệp

Một kiến trúc sư doanh nghiệp luân phiên đội ba chiếc mũ. Nhấn để lọc slide theo từng lăng kính (có thể chọn nhiều).

Nhà Quy hoạch

The Planner

Hiểu & định nghĩa EA: khái niệm, giá trị, các miền kiến trúc và lộ trình.

Năng lực: Kiến thức nền tảng EA

Nhà Kiến tạo

The Architect

Phát triển kiến trúc qua TOGAF ADM và bốn miền BDAT.

Năng lực: Kỹ năng Thiết kế EA

Nhà Điều phối

The Facilitator

Gắn kết stakeholder và vận dụng các kỹ thuật ADM.

Năng lực: Communication & Stakeholder Engagement

## Mở đầu

Slide 1–2

Trang bìa và bố cục ba module của khóa Enterprise Architecture — đặt ra 'sợi chỉ vàng' xuyên suốt: đi từ hiểu (What/Why) đến phương pháp (How) rồi công cụ (With what).

**Ý chính**

  * Khóa học gồm 3 module: Nền tảng EA → TOGAF & ADM → Kỹ thuật ADM.
  * Ba module phản ánh logic học tập: hiểu khái niệm, học phương pháp, rồi trang bị công cụ.

**Kiểm tra nhanh:**Khóa học gồm mấy module và tên là gì?

Ba: (1) EA Introduction & Fundamentals, (2) TOGAF & ADM, (3) ADM Technique.

Sợi chỉ vàng xuyên suốt EA là gì?

Chiến lược → Hiện trạng (Baseline) → Khoảng cách (Gap) → Mục tiêu (Target) → Lộ trình (Roadmap) → Giá trị.

### Trang bìa – Enterprise Architecture: Introduction & Example

**Mô tả nội dung**

Trang bìa khóa học Enterprise Architecture (Kiến trúc Doanh nghiệp) của chương trình CIO Vietnam – CIO Coaching, phụ đề 'Introduction & Example'.

**Diễn giải chi tiết**

Cái tên 'Enterprise Architecture' đã hàm chứa một lập trường: doanh nghiệp, giống như một thành phố, không nên để phát triển tự phát mà cần được 'quy hoạch' có chủ đích. Khóa học đi theo mạch của chuẩn TOGAF: trước hết là nền tảng khái niệm (EA là gì, vì sao cần), rồi đến phương pháp phát triển kiến trúc ADM, và cuối cùng là các kỹ thuật thực hành. Phụ đề 'Introduction & Example' báo hiệu cách tiếp cận: không chỉ lý thuyết mà luôn gắn với ví dụ thực tế để người học hình dung được cách áp dụng.

**Ví dụ**

Một CIO không chỉ 'mua và vận hành hệ thống' mà còn vẽ ra 'bản quy hoạch tổng thể' cho toàn bộ nghiệp vụ, dữ liệu, ứng dụng và công nghệ của doanh nghiệp — đó chính là tinh thần EA.

Câu hỏi thường gặpTài liệu này nói về chủ đề gì?

Đây là khóa giới thiệu Enterprise Architecture (Kiến trúc Doanh nghiệp – EA), cách định nghĩa, xây dựng và triển khai kiến trúc doanh nghiệp theo chuẩn TOGAF, kèm ví dụ minh họa.

EA viết tắt của cụm từ nào?

Enterprise Architecture – Kiến trúc Doanh nghiệp.

Đối tượng học của khóa này là ai?

Những người đảm nhiệm hoặc hướng tới vai trò kiến trúc sư doanh nghiệp, CIO/CTO, hoặc lãnh đạo cần hiểu cách gắn kết chiến lược kinh doanh với công nghệ.

**Mạch nối:** Trang bìa đã xác lập chủ đề. Slide tiếp theo mở ra bố cục ba module của toàn khóa để người học thấy lộ trình trước khi đi vào chi tiết.

### Outlines – Bố cục khóa học (3 Module)

**Mô tả nội dung**

Liệt kê ba module: Module 1 – EA Introduction & Fundamentals; Module 2 – TOGAF & Architecture Development Method (ADM); Module 3 – ADM Technique.

**Diễn giải chi tiết**

Ba module phản ánh một logic học tập có chủ đích: đi từ 'hiểu' (What & Why) sang 'phương pháp' (How) rồi tới 'công cụ' (With what). Module 1 đặt nền khái niệm — EA là gì, tạo giá trị gì, gồm những miền nào. Module 2 là trái tim của khóa học: phương pháp TOGAF ADM với chu trình Preliminary → A–H giúp phát triển kiến trúc một cách bài bản. Module 3 trang bị các kỹ thuật cụ thể (nguyên tắc kiến trúc, kịch bản nghiệp vụ, phân tích khoảng cách, quản lý stakeholder…) để thực thi ADM hiệu quả. Nắm bố cục này giúp người học biết mỗi kiến thức mới thuộc về chặng nào của hành trình.

**Ví dụ**

Giống như học xây nhà: trước hết hiểu 'nhà là gì và để làm gì' (M1), rồi học 'quy trình thiết kế & thi công' (M2), cuối cùng là 'bộ dụng cụ cụ thể' như thước, bản vẽ, phần mềm (M3).

Câu hỏi thường gặpKhóa học gồm mấy module?

Ba module: (1) Giới thiệu & Nền tảng EA, (2) TOGAF & Phương pháp Phát triển Kiến trúc ADM, (3) Kỹ thuật ADM.

Vì sao lại sắp xếp theo trình tự này?

Vì kiến thức xây dựng dần: hiểu khái niệm trước, rồi học phương pháp phát triển kiến trúc, cuối cùng là các kỹ thuật thực hành để áp dụng phương pháp đó.

ADM là gì?

Architecture Development Method – Phương pháp Phát triển Kiến trúc, chu trình lõi của TOGAF gồm giai đoạn Preliminary và các Phase A đến H.

**Mạch nối:** Bố cục đã rõ. Khóa học bắt đầu bằng Module 1 — phần đặt nền khái niệm, trả lời câu hỏi EA là gì và vì sao doanh nghiệp cần đến nó.

## Module 1 · Nền tảng EA

Slide 3–14

Đặt nền khái niệm: EA là gì, khi nào cần, tạo giá trị gì; giới thiệu năng lực EA, cách xây lộ trình, các miền kiến trúc (BDAT + Security) và truy vết xuyên suốt.

**Ý chính**

  * EA vừa là mô tả, vừa là khung quản lý thay đổi, vừa là thực hành — ví như 'quy hoạch đô thị' cho doanh nghiệp.
  * Kiến trúc luôn xoay quanh ba trạng thái: Baseline (hiện tại) – Gap (khoảng cách) – Target (mục tiêu).
  * Bốn miền BDAT + Security (xuyên suốt); truy vết nối chiến lược với công nghệ.

**Kiểm tra nhanh:**EA được ví với điều gì và vì sao?

Với quy hoạch đô thị — EA là 'bản quy hoạch thành phố' đặt khung & tiêu chuẩn chung để các dự án (tòa nhà) ăn khớp nhau.

Khoảng cách (gap) quan trọng thế nào?

Khoảng cách giữa hiện tại và tương lai chỉ ra chính xác điều gì phải thay đổi — là đầu vào để lập lộ trình.

Bốn miền kiến trúc lõi là gì?

Business, Data, Application, Technology (BDAT); Security là miền xuyên suốt cả bốn.

### Module 1 – EA Introduction & Fundamentals (Giới thiệu & Nền tảng)

**Mô tả nội dung**

Trang tiêu đề Module 1, liệt kê 5 nội dung: (1) Định nghĩa EA, (2) Cách định nghĩa một EA, (3) Năng lực EA, (4) Cách xây dựng Lộ trình EA, (5) Các miền kiến trúc.

**Diễn giải chi tiết**

Module 1 tạo ra một sự dịch chuyển trong cách nghĩ: từ chỗ coi CNTT là 'nơi mua sắm và vận hành hệ thống' sang chỗ coi kiến trúc doanh nghiệp là 'bản quy hoạch chiến lược' gắn kết mọi thay đổi với mục tiêu kinh doanh. Năm nội dung trả lời năm câu hỏi nối tiếp: EA là gì (định nghĩa), làm sao xác định phạm vi của nó (enterprise-wide vs project), năng lực EA gồm những gì, làm sao biến kiến trúc thành lộ trình hành động, và kiến trúc được phân thành những miền nào (Business, Data, Application, Technology, Security). Trình tự này đi từ khái niệm trừu tượng đến cấu trúc cụ thể.

**Ví dụ**

Thay vì xem EA là 'một bộ tài liệu Visio để trong ngăn kéo', module này giúp người học hiểu EA là công cụ sống để quản lý thay đổi và giảm rủi ro cho toàn doanh nghiệp.

Câu hỏi thường gặpModule 1 giới thiệu những nội dung gì?

Định nghĩa EA; cách định nghĩa/khoanh vùng một EA; năng lực EA; cách xây dựng lộ trình EA; và các miền kiến trúc (BDAT + Security).

Vì sao bắt đầu bằng phần nền tảng?

Để người học nắm khái niệm và giá trị của EA trước khi đi vào phương pháp TOGAF, tránh hiểu EA chỉ là công việc vẽ sơ đồ kỹ thuật.

**Mạch nối:** Module 1 đã mở ra với khung 5 nội dung. Slide tiếp theo đi thẳng vào nội dung đầu tiên và quan trọng nhất — định nghĩa Enterprise Architecture.

### Defining Enterprise Architecture – Định nghĩa EA

**Mô tả nội dung**

Ghép hai khái niệm: 'Enterprise' (tập hợp các tổ chức có mục tiêu chung) và 'Architecture' (cấu trúc các thành phần, quan hệ giữa chúng, cùng các nguyên tắc chi phối thiết kế và tiến hóa). EA vừa là mô tả, vừa là khung quản lý thay đổi, vừa là thực hành.

**Diễn giải chi tiết**

Định nghĩa EA có ba tầng bổ sung nhau. Thứ nhất, EA là một MÔ TẢ: các thành phần trong tổ chức là gì, nhằm đạt điều gì, được sắp xếp ra sao, vận hành thế nào và ứng phó với thay đổi như thế nào. Thứ hai, EA là một KHUNG (cấu trúc, cách tiếp cận, quy trình) để quản lý thay đổi các thành phần đó, giúp tổ chức liên tục thích nghi theo chiến lược (mục tiêu) và hoàn cảnh (yêu cầu cụ thể). Thứ ba, EA là một THỰC HÀNH — hành động quản lý và tiến hóa kiến trúc ở mọi cấp độ kiểm soát, thay đổi và nhịp độ. Điểm cốt lõi: EA cung cấp một 'tầm nhìn đủ' về tổ chức để quản lý sự phức tạp, hỗ trợ thay đổi liên tục và kiểm soát rủi ro của những hệ quả không lường trước.

Ví dụ ◨ có sơ đồ

Khi doanh nghiệp muốn triển khai hệ thống bán hàng đa kênh, EA cho biết thay đổi này chạm tới những quy trình, dữ liệu, ứng dụng và hạ tầng nào — nhờ đó lường trước được hệ quả thay vì 'vá lỗi' sau khi đã xảy ra.

Câu hỏi thường gặpEnterprise Architecture là gì?

Là mô tả các thành phần của tổ chức (mục tiêu, cách sắp xếp, cách vận hành, cách ứng phó thay đổi); đồng thời là một khung quản lý thay đổi và là một thực hành liên tục để tiến hóa kiến trúc theo chiến lược.

'Enterprise' và 'Architecture' nghĩa là gì?

Enterprise là bất kỳ tập hợp tổ chức nào có mục tiêu chung; Architecture là cấu trúc các thành phần, quan hệ giữa chúng và các nguyên tắc chi phối thiết kế, tiến hóa của chúng theo thời gian.

EA mang lại điều gì cốt lõi?

Một tầm nhìn đủ về tổ chức để quản lý sự phức tạp, hỗ trợ thay đổi liên tục và giảm rủi ro của những hệ quả không mong muốn — gắn với cả định hướng chiến lược lẫn giá trị kinh doanh.

**Mạch nối:** Đã có định nghĩa, câu hỏi tự nhiên là: mọi việc đều cần kiến trúc chính thức hay không? Slide tiếp theo trả lời khi nào thực sự cần đến một 'bản thiết kế kiến trúc'.

### Do we need an Architecture? – Khi nào cần kiến trúc?

**Mô tả nội dung**

Một bản thiết kế kiến trúc chính thức không phải lúc nào cũng cần thiết. Nhưng độ phức tạp của công việc càng lớn thì nhu cầu về một bản blueprint dẫn đường và lộ trình theo giai đoạn càng cao — cũng thiết yếu để phát triển thêm hay chỉnh sửa về sau.

**Diễn giải chi tiết**

Thông điệp then chốt: kiến trúc không miễn phí, nên phải cân nhắc chi phí – lợi ích theo độ phức tạp. Với một cái chuồng chó, ta không cần bản vẽ kiến trúc sư; nhưng với một tòa nhà chọc trời thì bản thiết kế và kế hoạch thi công theo giai đoạn là bắt buộc. Doanh nghiệp cũng vậy: hệ thống càng lớn, càng nhiều bên liên quan, càng nhiều phụ thuộc chằng chịt, thì rủi ro 'xây xong mới thấy sai' càng cao — và một bản kiến trúc dẫn đường giúp giảm rủi ro đó. Kiến trúc còn có giá trị lâu dài: nó là cơ sở để mở rộng, bảo trì và sửa đổi trong tương lai mà không phá vỡ tổng thể.

**Ví dụ**

Xây một landing page đơn giản thì không cần EA; nhưng chuyển đổi cả hệ thống ERP cho tập đoàn đa quốc gia thì thiếu kiến trúc gần như chắc chắn dẫn tới đội chi phí và trễ tiến độ.

Câu hỏi thường gặpCó phải mọi dự án đều cần kiến trúc chính thức không?

Không. Với công việc đơn giản, một blueprint chính thức có thể không cần thiết để xây dựng và bảo trì thành công.

Khi nào kiến trúc trở nên cần thiết?

Khi độ phức tạp tăng lên — càng phức tạp thì càng cần một blueprint dẫn đường và lộ trình theo giai đoạn, cũng để phục vụ phát triển và chỉnh sửa về sau.

**Mạch nối:** Khi đã xác định cần kiến trúc, câu hỏi kế tiếp là làm sao khoanh vùng nó cho đúng. Slide sau phân biệt góc nhìn toàn doanh nghiệp và góc nhìn dự án qua ẩn dụ quy hoạch đô thị.

### How to define an EA? – Toàn doanh nghiệp vs Dự án (ẩn dụ Quy hoạch Đô thị)

PD

**Mô tả nội dung**

So sánh hai góc nhìn: 'Enterprise-wide focus' (Chiến lược & Quản trị, Kiến trúc dịch vụ/quy trình/con người + IS/IT) và 'Project focus' (Chiến lược IT, giải pháp IT). EA được ví như 'bản quy hoạch thành phố', còn Solution là 'thiết kế từng tòa nhà'.

**Diễn giải chi tiết**

Đây là một trong những ẩn dụ mạnh nhất của EA: kiến trúc doanh nghiệp giống quy hoạch đô thị. Bản quy hoạch thành phố (EA) quyết định đường sá, điện nước, phân khu chức năng, tiêu chuẩn chung — trong khi thiết kế từng tòa nhà (Solution) tự do sáng tạo nhưng phải tuân thủ quy hoạch. Góc nhìn toàn doanh nghiệp bao trùm Chiến lược & Quản trị, kiến trúc nghiệp vụ (dịch vụ, quy trình, con người) và kiến trúc IS/IT (thông tin, ứng dụng, công nghệ), cùng lập kế hoạch chuyển tiếp (Transition Planning). Góc nhìn dự án hẹp hơn, chỉ tập trung vào giải pháp IT cho một nhu cầu cụ thể. Sự phân biệt này giúp EA làm đúng vai: định hình khung tổng thể để mọi dự án 'gắn khớp' vào nhau thay vì mỗi dự án tự xây theo cách riêng.

Ví dụ ◨ có sơ đồ

Nếu mỗi phòng ban tự mua một phần mềm quản lý khách hàng khác nhau (project focus, không có quy hoạch), doanh nghiệp sẽ có 5 'kho dữ liệu khách hàng' rời rạc — đúng kiểu thành phố không quy hoạch với đường sá chồng chéo.

Câu hỏi thường gặpEA khác Solution ở điểm nào?

EA là 'bản quy hoạch thành phố' — khung tổng thể cấp doanh nghiệp; Solution là 'thiết kế từng tòa nhà' — giải pháp cho một dự án cụ thể phải tuân theo quy hoạch đó.

Góc nhìn toàn doanh nghiệp bao gồm gì?

Chiến lược & Quản trị, kiến trúc nghiệp vụ (dịch vụ, quy trình, con người), kiến trúc IS/IT (thông tin, ứng dụng, công nghệ) và lập kế hoạch chuyển tiếp.

Vì sao ẩn dụ quy hoạch đô thị hữu ích?

Vì nó cho thấy EA đặt ra khung và tiêu chuẩn chung để các dự án riêng lẻ ăn khớp với nhau, tránh trùng lắp và mâu thuẫn.

**Mạch nối:** Ẩn dụ quy hoạch đã cho thấy vai trò của EA. Slide tiếp theo làm rõ giá trị đó bằng cách so sánh một thành phố có và không có tư duy kiến trúc.

### Value of Architecture Thinking – Giá trị của tư duy kiến trúc

**Mô tả nội dung**

So sánh hai kịch bản: thành phố KHÔNG quy hoạch (giao thông, trường học, công viên chỉ là 'suy nghĩ thêm'; không dịch vụ chung; quy trình phân mảnh, kém hiệu quả; kém thẩm mỹ; hạn chế tăng trưởng) và thành phố CÓ quy hoạch (hướng tương lai, bền vững; dịch vụ chung; nguyên tắc & tiêu chuẩn; năng suất cao; thẩm mỹ tốt).

**Diễn giải chi tiết**

Slide biến ẩn dụ quy hoạch thành một luận chứng giá trị cụ thể. Không có tư duy kiến trúc, doanh nghiệp giống một khu đô thị mọc lên tự phát: các dịch vụ dùng chung (như hạ tầng, dữ liệu chuẩn) bị bỏ quên, quy trình chồng chéo và kém hiệu quả, khó mở rộng khi cần tăng trưởng. Có tư duy kiến trúc, doanh nghiệp có định hướng tương lai, các dịch vụ dùng chung được thiết kế từ đầu, có nguyên tắc và tiêu chuẩn (an toàn, phòng cháy, quy hoạch tổng thể) làm nền, từ đó năng suất và hiệu quả cao hơn. Bài học: giá trị của EA không nằm ở bản vẽ đẹp, mà ở khả năng ngăn ngừa lãng phí và mở đường cho tăng trưởng bền vững.

**Ví dụ**

Một tập đoàn thiết kế nền tảng dữ liệu khách hàng dùng chung (common service) ngay từ đầu sẽ tránh được cảnh 10 hệ thống mỗi cái giữ một phiên bản thông tin khách hàng khác nhau.

Câu hỏi thường gặpThành phố không quy hoạch có những vấn đề gì?

Dịch vụ công là 'suy nghĩ thêm', không có dịch vụ dùng chung, quy trình phân mảnh và kém hiệu quả, kém thẩm mỹ và hạn chế khả năng tăng trưởng.

Tư duy kiến trúc mang lại gì?

Định hướng tương lai và bền vững, dịch vụ dùng chung, nguyên tắc & tiêu chuẩn rõ ràng, năng suất và hiệu quả cao hơn.

**Mạch nối:** Giá trị đã rõ, nhưng EA không hoạt động đơn độc. Slide tiếp theo đặt EA vào bức tranh lớn hơn của các khung quản trị doanh nghiệp và mối liên hệ giữa chúng.

### Interoperability between Management Frameworks – Liên thông giữa các khung quản trị

PD

**Mô tả nội dung**

Sơ đồ thể hiện mối quan hệ và tính liên thông (interoperability) giữa các khung quản lý: chiến lược, kiến trúc doanh nghiệp, quản trị danh mục/chương trình/dự án, quản trị dịch vụ, quản trị rủi ro/an toàn…

**Diễn giải chi tiết**

EA không thay thế mà kết nối các khung quản trị hiện có. Chiến lược đặt ra định hướng; EA chuyển định hướng đó thành cấu trúc và lộ trình; quản trị danh mục/chương trình/dự án (như PMI, PRINCE2) hiện thực hóa lộ trình; quản trị dịch vụ (như ITIL) vận hành kết quả; quản trị rủi ro và an toàn bao trùm tất cả. Điểm mấu chốt là tính liên thông: các khung này phải 'nói chuyện' được với nhau, dùng chung ngôn ngữ và dữ liệu, để không tạo ra các silo quản trị mâu thuẫn. EA đóng vai trò cầu nối, đảm bảo mọi khung cùng phục vụ một chiến lược thống nhất.

**Ví dụ**

Một quyết định kiến trúc (chọn nền tảng cloud) phải liên thông với quản trị danh mục đầu tư (ngân sách), quản trị dịch vụ (vận hành ITIL) và quản trị rủi ro (bảo mật dữ liệu) — nếu tách rời, dự án dễ mâu thuẫn nội bộ.

Câu hỏi thường gặpVì sao cần liên thông giữa các khung quản trị?

Để tránh silo quản trị mâu thuẫn; các khung chiến lược, kiến trúc, dự án, dịch vụ và rủi ro phải phối hợp và dùng chung ngôn ngữ để cùng phục vụ một chiến lược.

EA đóng vai trò gì giữa các khung này?

EA là cầu nối chuyển chiến lược thành cấu trúc và lộ trình, kết nối các khung quản trị lại với nhau thay vì thay thế chúng.

**Mạch nối:** Để 'điều phối' được các khung này và dẫn dắt thay đổi, doanh nghiệp cần một năng lực kiến trúc riêng. Slide tiếp theo giới thiệu khái niệm Năng lực EA.

### Architecture Capability (EA Capability) – Năng lực Kiến trúc

**Mô tả nội dung**

EA dùng để mô tả trạng thái tương lai của doanh nghiệp nhằm dẫn dắt thay đổi hướng tới trạng thái đó. Mô tả trạng thái tương lai giúp mọi người hiểu điều gì phải có để đạt mục tiêu, sứ mệnh, tầm nhìn; và khoảng cách giữa hiện tại và tương lai làm nổi bật điều phải thay đổi.

**Diễn giải chi tiết**

Đây là 'sợi chỉ vàng' của toàn bộ EA, được nêu ngay từ Module 1: kiến trúc luôn xoay quanh ba trạng thái — Hiện tại (Baseline), Tương lai (Target) và Khoảng cách (Gap) giữa chúng. EA mô tả rõ trạng thái tương lai để những người then chốt hiểu doanh nghiệp cần có gì mới nhằm đạt mục tiêu, sứ mệnh và tầm nhìn, trong bối cảnh cụ thể mà nó vận hành. Chính khoảng cách giữa hiện tại và tương lai mới là thứ chỉ ra điều gì phải thay đổi — và đó là đầu vào để lập lộ trình. Năng lực EA (EA Capability) là toàn bộ khả năng (con người, quy trình, công cụ, quản trị) để làm được việc mô tả – so sánh – dẫn dắt thay đổi này một cách liên tục.

Ví dụ ◨ có sơ đồ

Nếu 'trạng thái tương lai' là bán hàng đa kênh thời gian thực, còn 'hiện tại' là các kênh rời rạc cập nhật cuối ngày, thì khoảng cách chính là những gì cần xây: tích hợp dữ liệu thời gian thực, chuẩn API chung…

Câu hỏi thường gặpEA Capability (Năng lực EA) dùng để làm gì?

Để mô tả trạng thái tương lai của doanh nghiệp và dẫn dắt thay đổi tiến tới trạng thái đó.

Vì sao 'khoảng cách' (gap) lại quan trọng?

Vì khoảng cách giữa trạng thái hiện tại và tương lai chỉ ra chính xác điều gì phải thay đổi trong doanh nghiệp — là cơ sở để lập kế hoạch.

Mô tả trạng thái tương lai giúp ích gì?

Giúp những người then chốt hiểu điều gì phải có trong doanh nghiệp để đạt mục tiêu, sứ mệnh và tầm nhìn trong bối cảnh vận hành cụ thể.

**Mạch nối:** Khoảng cách giữa hiện tại và tương lai cần được biến thành hành động có thứ tự. Slide tiếp theo giới thiệu cách xây dựng Lộ trình EA — chính là cây cầu bắc qua khoảng cách đó.

### How to build an EA Roadmap – Xây dựng Lộ trình EA

PD

**Mô tả nội dung**

Sáu bước: (1) Xác định trạng thái hiện tại, (2) Định nghĩa trạng thái mong muốn, (3) Phân tích khoảng cách, (4) Ưu tiên các hạng mục hành động, (5) Tìm trình tự tốt nhất, (6) Phát triển & công bố lộ trình. Roadmap là bản blueprint chiến lược truyền đạt cách kế hoạch IT giúp đạt mục tiêu kinh doanh.

**Diễn giải chi tiết**

Lộ trình EA là công cụ biến kiến trúc từ 'bức tranh tĩnh' thành 'kế hoạch hành động'. Sáu bước tạo thành một quy trình logic: nắm hiện trạng → xác định đích đến → đo khoảng cách → ưu tiên việc cần làm → sắp trình tự hợp lý (tính đến phụ thuộc) → công bố. Ba lợi ích nổi bật: giúp giành được sự ủng hộ của các bên liên quan (buy-in); là công cụ linh hoạt để chia sẻ đúng mức chi tiết cho từng nhóm khán giả; và giúp đội ngũ bám đúng ưu tiên chiến lược. Về thời điểm: EA nên được làm SỚM và XUYÊN SUỐT quá trình thay đổi để giúp người ra quyết định hiểu hệ quả — nếu làm sau khi đã quyết, EA chỉ còn là tài liệu ghi lại quyết định chứ không còn giá trị định hướng.

**Ví dụ**

Một CIO trình bày roadmap 3 năm: năm 1 chuẩn hóa dữ liệu, năm 2 tích hợp ứng dụng lõi, năm 3 mở nền tảng số cho khách hàng — mỗi giai đoạn gắn với một mục tiêu kinh doanh cụ thể để lãnh đạo dễ phê duyệt.

Câu hỏi thường gặpSáu bước xây dựng lộ trình EA là gì?

Xác định hiện trạng; định nghĩa trạng thái mong muốn; phân tích khoảng cách; ưu tiên hạng mục hành động; tìm trình tự tốt nhất; phát triển và công bố lộ trình.

Lộ trình EA mang lại lợi ích gì?

Giành sự ủng hộ của các bên liên quan; là công cụ linh hoạt chia sẻ đúng mức chi tiết cho từng nhóm; giúp đội ngũ bám đúng ưu tiên chiến lược.

Khi nào nên làm EA?

Càng sớm càng tốt và xuyên suốt quá trình thay đổi. Nếu làm sau khi đã ra quyết định, EA chỉ còn là tài liệu ghi lại chứ không định hướng được nữa.

**Mạch nối:** Lộ trình cho thấy EA hành động ra sao. Slide tiếp theo tổng kết những lợi ích cụ thể mà EA mang lại cho doanh nghiệp.

### Benefits of Enterprise Architecture – Lợi ích của EA

**Mô tả nội dung**

Năm nhóm lợi ích: (1) Ra quyết định chiến lược hiệu quả hơn cho lãnh đạo C-Level; (2) ROI tốt hơn trên đầu tư hiện có, giảm rủi ro cho đầu tư tương lai; (3) Vận hành nghiệp vụ hiệu quả hơn; (4) Mua sắm nhanh, đơn giản, rẻ hơn; (5) Chuyển đổi số và vận hành hiệu quả hơn. (Nguồn: TOGAF Standard).

**Diễn giải chi tiết**

Lợi ích của EA trải khắp các cấp: ở cấp chiến lược, EA cho lãnh đạo một bức tranh tổng thể để quyết định sáng suốt hơn; ở cấp tài chính, EA giúp tận dụng tốt đầu tư đã có và giảm rủi ro cho đầu tư mới (tránh mua trùng, tránh chọn công nghệ ngõ cụt); ở cấp vận hành, EA làm quy trình gọn và hiệu quả hơn; ở khâu mua sắm, EA giúp mua nhanh – đơn giản – rẻ vì có tiêu chuẩn và danh mục rõ ràng; và ở chuyển đổi số, EA là bản đồ giúp thay đổi có định hướng thay vì chắp vá. Điểm chung của mọi lợi ích: chúng đến từ việc EA giảm sự phức tạp và mang lại tầm nhìn tổng thể.

**Ví dụ**

Nhờ có kiến trúc chuẩn, khi cần mua thêm phần mềm, doanh nghiệp chỉ chọn từ danh mục công nghệ đã được phê duyệt — mua nhanh hơn, rẻ hơn và không tạo ra 'ốc đảo công nghệ' mới.

Câu hỏi thường gặpEA mang lại những lợi ích chính nào?

Quyết định chiến lược tốt hơn; ROI cao hơn và giảm rủi ro đầu tư; vận hành hiệu quả hơn; mua sắm nhanh–đơn giản–rẻ hơn; chuyển đổi số hiệu quả hơn.

Vì sao EA giúp giảm rủi ro đầu tư?

Vì EA cho tầm nhìn tổng thể để tránh mua trùng lắp, tránh chọn công nghệ ngõ cụt và đảm bảo đầu tư mới ăn khớp với kiến trúc chung.

**Mạch nối:** Để hiện thực hóa những lợi ích này, kiến trúc cần được phân rã thành các miền quản lý được. Slide tiếp theo giới thiệu các Miền Kiến trúc.

### Architecture Domain – Các miền kiến trúc (BDAT + Security)

PD

**Mô tả nội dung**

Bốn miền lõi: Business (chiến lược, quản trị, tổ chức, quy trình nghiệp vụ); Data (cấu trúc tài sản dữ liệu logic/vật lý và quản lý dữ liệu); Application (bản thiết kế các ứng dụng, tương tác và quan hệ với quy trình); Technology (kiến trúc số, hạ tầng phần mềm/phần cứng và tiêu chuẩn). Cộng thêm Security (miền xuyên suốt để đạt và duy trì rủi ro được kiểm soát).

**Diễn giải chi tiết**

Phân miền kiến trúc là cách 'chia để trị' sự phức tạp của doanh nghiệp. Bốn miền BDAT xếp theo tầng từ nghiệp vụ xuống công nghệ: Business định nghĩa doanh nghiệp làm gì và làm thế nào; Data mô tả doanh nghiệp cần dữ liệu gì; Application cho biết ứng dụng nào xử lý dữ liệu và phục vụ quy trình; Technology mô tả hạ tầng chạy các ứng dụng đó. Security là miền đặc biệt — nó xuyên suốt cả bốn miền còn lại (cross-cutting) chứ không nằm riêng một tầng. Ngoài ra, có thể định nghĩa nhiều miền phái sinh bằng cách kết hợp các góc nhìn BDAT, ví dụ Kiến trúc Thông tin, Kiến trúc Rủi ro & An toàn, hay Kiến trúc Số. Cách phân miền này giúp mỗi nhóm chuyên gia tập trung đúng phần việc mà vẫn giữ được sự liên kết tổng thể.

**Ví dụ**

Khi số hóa quy trình duyệt vay: Business định nghĩa quy trình duyệt; Data là hồ sơ khách hàng; Application là hệ thống chấm điểm tín dụng; Technology là máy chủ/cloud; Security bao trùm việc bảo vệ dữ liệu nhạy cảm ở mọi tầng.

Câu hỏi thường gặpBốn miền kiến trúc lõi là gì?

Business (Nghiệp vụ), Data (Dữ liệu), Application (Ứng dụng) và Technology (Công nghệ) — thường viết tắt là BDAT.

Miền Security khác gì bốn miền còn lại?

Security là miền xuyên suốt (cross-cutting), tương tác với cả bốn miền BDAT để đạt và duy trì trạng thái rủi ro được kiểm soát, chứ không nằm riêng một tầng.

Có thể có thêm miền nào khác không?

Có — bằng cách kết hợp các góc nhìn BDAT, ví dụ Kiến trúc Thông tin, Kiến trúc Rủi ro & An toàn, Kiến trúc Số.

**Mạch nối:** Sau khi biết có những miền nào, slide tiếp theo đi sâu hơn vào chi tiết bên trong từng miền và cách chúng liên kết.

### Architecture Domain in Detail – Chi tiết các miền kiến trúc

PD

**Mô tả nội dung**

Trình bày chi tiết hơn các thành phần bên trong mỗi miền BDAT và cách chúng liên kết theo tầng, từ nghiệp vụ (trên cùng) xuống công nghệ (dưới cùng).

**Diễn giải chi tiết**

Slide này 'phóng to' cấu trúc bên trong bốn miền để thấy chúng không rời rạc mà xếp chồng và phụ thuộc lẫn nhau theo chiều dọc. Miền Business ở trên cùng gồm các năng lực, quy trình, tổ chức và vai trò. Miền Data mô tả các thực thể dữ liệu và luồng dữ liệu phục vụ quy trình. Miền Application gồm các thành phần ứng dụng (được nhìn như nhóm năng lực logic, không phải phần mềm cụ thể) xử lý dữ liệu và hỗ trợ quy trình. Miền Technology ở dưới cùng là hạ tầng nền chạy tất cả. Sự phụ thuộc theo tầng này chính là cơ sở cho 'truy vết' (traceability): thay đổi ở một tầng lan tỏa tới các tầng khác, và EA giúp nhìn thấy sự lan tỏa đó.

**Ví dụ**

Một thực thể dữ liệu 'Đơn hàng' (Data) được tạo bởi quy trình 'Đặt hàng' (Business), xử lý bởi ứng dụng 'OMS' (Application), lưu trên hạ tầng cloud (Technology) — bốn tầng gắn với nhau qua một dòng nghiệp vụ.

Câu hỏi thường gặpCác miền kiến trúc liên kết với nhau ra sao?

Theo tầng dọc: Business ở trên định hướng, Data và Application ở giữa phục vụ nghiệp vụ, Technology ở dưới làm nền — mỗi tầng phụ thuộc vào tầng liền kề.

Vì sao cần nhìn chi tiết bên trong từng miền?

Để thấy các thành phần cụ thể (năng lực, thực thể dữ liệu, ứng dụng, hạ tầng) và cách thay đổi ở một tầng ảnh hưởng tới các tầng khác — nền tảng cho truy vết.

**Mạch nối:** Sự phụ thuộc theo tầng dẫn tới một năng lực quan trọng: truy vết xuyên suốt. Slide tiếp theo trình bày Truy vết Kiến trúc Doanh nghiệp — cách nối chiến lược với công nghệ.

### Traceability EA – Truy vết & Thu hẹp khoảng cách Business–IT

PD

**Mô tả nội dung**

Truy vết giải quyết bài toán lệch pha chuyển đổi số bằng cách thiết lập các liên kết truy vết ngang và chéo. Chiều dọc: phân rã nghiệp vụ từ trừu tượng đến chi tiết (không tạo quy trình/dữ liệu/vai trò nào mà không phục vụ một Năng lực Nghiệp vụ cấp cao). Chiều ngang: ánh xạ giải pháp IT vào nhu cầu nghiệp vụ.

**Diễn giải chi tiết**

Truy vết (traceability) là năng lực 'nhìn xuyên' các tầng kiến trúc để trả lời câu hỏi: thay đổi chỗ này ảnh hưởng chỗ nào? Nó thiết lập liên kết theo hai chiều. Chiều dọc bảo đảm mọi quy trình, dữ liệu, vai trò được tạo ra đều phục vụ một Năng lực Nghiệp vụ ở cấp cao nhất — không có thành phần 'mồ côi' không rõ mục đích. Chiều ngang bảo đảm mọi giải pháp IT đều ánh xạ trực tiếp hoặc gián tiếp tới một yêu cầu nghiệp vụ tương ứng, giữ cho IT luôn liên quan. Lợi ích tối đa của truy vết gồm: tầm nhìn xuyên suốt từ chiến lược đến giá trị; phân tích tác động qua mọi tầng kiến trúc; quyết định và gắn kết đầu tư tốt hơn; giảm rủi ro, trùng lắp và nợ kỹ thuật; sẵn sàng tuân thủ – quản trị – kiểm toán; và một doanh nghiệp linh hoạt, bền bỉ, sẵn sàng cho tương lai.

**Ví dụ**

Khi lãnh đạo hỏi 'nếu bỏ hệ thống A thì ảnh hưởng gì?', nhờ truy vết, kiến trúc sư lập tức chỉ ra A phục vụ 3 quy trình, 2 năng lực nghiệp vụ và liên quan 5 hệ thống khác — thay vì đoán mò.

Câu hỏi thường gặpTruy vết (traceability) trong EA là gì?

Là việc thiết lập các liên kết ngang và chéo giữa nghiệp vụ và công nghệ để tức thời đánh giá tác động business-to-technology và ngược lại.

Chiều dọc và chiều ngang khác nhau ra sao?

Chiều dọc phân rã nghiệp vụ từ trừu tượng đến chi tiết (mọi thứ phải phục vụ một năng lực nghiệp vụ cấp cao); chiều ngang ánh xạ mọi giải pháp IT vào một nhu cầu nghiệp vụ.

Truy vết mang lại lợi ích gì?

Tầm nhìn end-to-end từ chiến lược đến giá trị; phân tích tác động; quyết định & gắn kết đầu tư tốt hơn; giảm rủi ro, trùng lắp, nợ kỹ thuật; sẵn sàng tuân thủ; doanh nghiệp linh hoạt và bền bỉ.

**Mạch nối:** Module 1 đã trang bị đầy đủ nền tảng khái niệm EA. Khóa học bước vào Module 2 — nơi giới thiệu phương pháp chuẩn để thực sự phát triển kiến trúc: TOGAF và ADM.
