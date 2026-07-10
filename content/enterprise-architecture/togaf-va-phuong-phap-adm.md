---
title: "TOGAF & Phương pháp Phát triển Kiến trúc (ADM)"
weight: 12
---

## Module 2 · TOGAF & ADM

Slide 15–62

Trái tim của khóa học — phương pháp TOGAF ADM: giai đoạn Preliminary, các Phase A–H, Requirements Management ở trung tâm, cùng Content Framework và Kiến trúc An toàn xuyên suốt.

**Ý chính**

  * ADM là chu trình lặp: Preliminary → A (Vision) → B (Business) → C (Info Systems) → D (Technology) → E (Opportunities) → F (Migration) → G (Governance) → H (Change).
  * Mỗi phase kiến trúc dùng chung khuôn 9 bước: Baseline → Target → Gap → thành phần lộ trình.
  * Requirements Management ở trung tâm — quy trình động, kết nối mọi phase; Security là miền cross-cutting.

**Kiểm tra nhanh:**Kể tên các giai đoạn ADM theo thứ tự.

Preliminary, A (Vision), B (Business), C (Information Systems), D (Technology), E (Opportunities & Solutions), F (Migration Planning), G (Implementation Governance), H (Change Management).

Vì sao ADM phát triển kiến trúc theo thứ tự B→C→D?

Vì 'nghiệp vụ dẫn dắt, công nghệ theo sau' — rõ nghiệp vụ trước, rồi dữ liệu/ứng dụng, cuối cùng mới chọn công nghệ.

Requirements Management nằm ở đâu và có tính chất gì?

Ở trung tâm ADM; là quy trình động, liên tục nạp/trả yêu cầu cho mọi phase, không phải tập yêu cầu tĩnh.

### Module 2 – TOGAF Framework & ADM

**Mô tả nội dung**

Trang tiêu đề Module 2, liệt kê nội dung: TOGAF Standard; Phương pháp Phát triển Kiến trúc (ADM); Tổng quan Content Framework; giai đoạn Preliminary; các Phase A–H.

**Diễn giải chi tiết**

Module 2 là trái tim của khóa học: nó chuyển từ 'hiểu EA là gì' sang 'làm EA thế nào' bằng một phương pháp chuẩn được công nhận toàn cầu — TOGAF của The Open Group. Trọng tâm là ADM (Architecture Development Method), một chu trình lặp gồm giai đoạn chuẩn bị (Preliminary) và tám giai đoạn A–H, với Quản lý Yêu cầu (Requirements Management) ở trung tâm điều phối. Module cũng giới thiệu Content Framework — bộ 'từ vựng' chuẩn về các sản phẩm kiến trúc (deliverables, artifacts, building blocks). Nắm ADM giúp người học có một 'công thức' bài bản để không bỏ sót bước nào khi phát triển kiến trúc.

**Ví dụ**

Giống như một đầu bếp chuyên nghiệp làm theo công thức chuẩn thay vì 'nấu theo cảm giác', kiến trúc sư dùng ADM để đảm bảo mọi giai đoạn từ tầm nhìn đến quản trị thay đổi đều được thực hiện đúng thứ tự.

Câu hỏi thường gặpTOGAF là gì?

The Open Group Architecture Framework — khung kiến trúc doanh nghiệp chuẩn phổ biến nhất thế giới, do The Open Group phát triển.

ADM gồm những gì?

Giai đoạn Preliminary (chuẩn bị) và tám giai đoạn Phase A đến H, với Requirements Management (Quản lý Yêu cầu) ở trung tâm.

Content Framework để làm gì?

Cung cấp bộ 'từ vựng' và cấu trúc chuẩn cho các sản phẩm kiến trúc — deliverables, artifacts và building blocks.

**Mạch nối:** Trước khi đi vào phương pháp, slide tiếp theo giới thiệu chính bộ chuẩn TOGAF phiên bản mới nhất — nền tảng cho toàn bộ Module 2.

### The TOGAF® Standard, 10th Edition – Chuẩn TOGAF phiên bản 10

**Mô tả nội dung**

Giới thiệu TOGAF Standard phiên bản thứ 10 của The Open Group — bộ chuẩn kiến trúc doanh nghiệp được cấu trúc lại theo dạng module để dễ áp dụng linh hoạt.

**Diễn giải chi tiết**

TOGAF phiên bản 10 (10th Edition) là bản chuẩn hiện hành, được tổ chức lại theo hướng 'modular' — tách phần lõi ổn định (ADM, khái niệm nền tảng) khỏi các hướng dẫn (guides) áp dụng cho từng bối cảnh cụ thể như Agile, số hóa, hay ngành nghề riêng. Cách cấu trúc này giúp doanh nghiệp 'may đo' (tailor) TOGAF cho phù hợp thay vì áp dụng cứng nhắc toàn bộ. Điểm cần nhớ: TOGAF là một khung (framework) chứ không phải một quy trình cứng — nó cung cấp phương pháp, ngôn ngữ chung và các mẫu, còn cách áp dụng cụ thể do tổ chức quyết định.

**Ví dụ**

Một ngân hàng có thể dùng phần lõi ADM của TOGAF 10 nhưng ghép thêm hướng dẫn 'TOGAF cho Agile' để phù hợp với đội phát triển sản phẩm theo sprint.

Câu hỏi thường gặpTOGAF phiên bản mới nhất là gì?

Phiên bản thứ 10 (10th Edition) của The Open Group.

Điểm mới của cách cấu trúc TOGAF 10 là gì?

Được tổ chức theo dạng module — tách phần lõi ổn định khỏi các hướng dẫn áp dụng, giúp tailor linh hoạt cho từng bối cảnh.

TOGAF là quy trình cứng hay khung linh hoạt?

Là một khung (framework) linh hoạt — cung cấp phương pháp, ngôn ngữ chung và mẫu, còn cách áp dụng do tổ chức tự tailor.

**Mạch nối:** Sau khi biết bộ chuẩn, slide tiếp theo giới thiệu tổng quan cấu trúc của khung TOGAF trước khi đi sâu vào chu trình ADM.

### TOGAF Framework – Tổng quan khung TOGAF

**Mô tả nội dung**

Trình bày tổng quan cấu trúc khung TOGAF: phần lõi ADM, các kỹ thuật và hướng dẫn (Guidelines & Techniques), Content Framework, Enterprise Continuum & Repository, và mô hình Năng lực Kiến trúc (Architecture Capability).

**Diễn giải chi tiết**

Khung TOGAF gồm nhiều thành phần phối hợp. ADM là phương pháp lõi — chu trình phát triển kiến trúc. Guidelines & Techniques cung cấp các kỹ thuật hỗ trợ áp dụng ADM (như nguyên tắc kiến trúc, phân tích khoảng cách…). Content Framework định nghĩa các sản phẩm đầu ra. Enterprise Continuum & Repository là 'thư viện' lưu trữ và phân loại các tài sản kiến trúc từ tổng quát đến cụ thể, để tái sử dụng. Architecture Capability Framework mô tả cách thiết lập và vận hành năng lực kiến trúc trong tổ chức (con người, vai trò, quản trị). Hiểu bức tranh tổng thể này giúp người học thấy ADM không đứng một mình mà được đỡ bởi cả một hệ sinh thái công cụ.

**Ví dụ**

Khi làm một dự án mới, kiến trúc sư dùng ADM làm phương pháp, tra Enterprise Continuum để tái sử dụng mẫu kiến trúc cũ, và tuân theo Content Framework khi viết tài liệu.

Câu hỏi thường gặpKhung TOGAF gồm những thành phần chính nào?

ADM (phương pháp lõi), Guidelines & Techniques, Content Framework, Enterprise Continuum & Repository, và Architecture Capability Framework.

Enterprise Continuum là gì?

Một cách phân loại và lưu trữ các tài sản kiến trúc từ tổng quát đến cụ thể, giúp tái sử dụng thay vì làm lại từ đầu.

**Mạch nối:** Trung tâm của khung là phương pháp phát triển kiến trúc. Slide tiếp theo trình bày chi tiết chu trình ADM — 'động cơ' của TOGAF.

### TOGAF ADM – Chu trình Phát triển Kiến trúc

**Mô tả nội dung**

Chu trình ADM dạng bánh xe: Preliminary (chuẩn bị) ở ngoài; Phase A – Architecture Vision; B – Business; C – Information Systems (Data & Application); D – Technology; E – Opportunities & Solutions; F – Migration Planning; G – Implementation Governance; H – Architecture Change Management; và Requirements Management ở trung tâm.

**Diễn giải chi tiết**

ADM là chuỗi giai đoạn lặp, mỗi giai đoạn có mục tiêu riêng nhưng nối tiếp nhau thành một vòng tuần hoàn. Preliminary chuẩn bị năng lực kiến trúc và định nghĩa các Nguyên tắc Kiến trúc. Phase A tạo Tầm nhìn Kiến trúc — xác định phạm vi, stakeholder và giá trị kỳ vọng. Phase B, C, D lần lượt phát triển kiến trúc Nghiệp vụ, Hệ thống Thông tin (Dữ liệu & Ứng dụng), và Công nghệ. Phase E xác định cơ hội & giải pháp và các Kiến trúc Chuyển tiếp. Phase F lập kế hoạch di trú chi tiết. Phase G giám sát việc triển khai đúng kiến trúc mục tiêu. Phase H quản lý thay đổi đối với kiến trúc mới. Ở trung tâm, Requirements Management vận hành liên tục — mọi giai đoạn đều lấy yêu cầu từ đây và trả yêu cầu về đây. Đặc điểm quan trọng: ADM lặp (iterative), có thể quay vòng và chạy lại từng phần khi cần.

Ví dụ ◨ có sơ đồ

Một dự án chuyển đổi kho hàng: Phase A đặt tầm nhìn WMS mới; B thiết kế lại quy trình kho; C thiết kế dữ liệu & ứng dụng WMS; D chọn hạ tầng; E–F lập lộ trình triển khai; G giám sát nhà thầu làm đúng; H quản lý các thay đổi phát sinh sau go-live.

Câu hỏi thường gặpADM gồm những giai đoạn nào?

Preliminary, rồi Phase A (Vision), B (Business), C (Information Systems), D (Technology), E (Opportunities & Solutions), F (Migration Planning), G (Implementation Governance), H (Change Management).

Requirements Management nằm ở đâu?

Ở trung tâm chu trình — vận hành liên tục, cấp và nhận yêu cầu từ mọi giai đoạn của ADM.

ADM có phải chạy một lần theo thứ tự cứng không?

Không — ADM là chu trình lặp (iterative), có thể quay vòng, chạy lại từng phần và điều chỉnh phạm vi theo nhu cầu.

**Mạch nối:** Chu trình ADM cần một bộ 'từ vựng' chuẩn cho các sản phẩm đầu ra. Slide tiếp theo giới thiệu Content Framework — nội dung mà mỗi giai đoạn tạo ra.

### Content Framework Overview – Tổng quan Khung Nội dung

**Mô tả nội dung**

Content Framework định nghĩa cấu trúc chuẩn các sản phẩm kiến trúc: Deliverables (sản phẩm bàn giao chính thức), Artifacts (tạo phẩm mô tả kiến trúc: catalog, matrix, diagram) và Building Blocks (khối kiến trúc: ABB – Architecture Building Block, SBB – Solution Building Block).

**Diễn giải chi tiết**

Content Framework trả lời câu hỏi: mỗi giai đoạn ADM tạo ra 'cái gì' và mô tả chúng theo chuẩn nào. Có ba loại sản phẩm. Deliverables là các sản phẩm bàn giao chính thức, được ký duyệt qua hợp đồng/dự án (ví dụ Statement of Architecture Work, Architecture Definition Document). Artifacts là các tạo phẩm mô tả kiến trúc, chia thành ba dạng: Catalog (danh mục các thành phần), Matrix (ma trận quan hệ giữa các thành phần) và Diagram (sơ đồ trực quan). Building Blocks là các khối kiến trúc tái sử dụng: ABB (Architecture Building Block) là khối logic độc lập công nghệ, còn SBB (Solution Building Block) là khối giải pháp cụ thể hiện thực hóa ABB. Bộ từ vựng chung này giúp các kiến trúc sư khác nhau tạo ra tài liệu nhất quán, dễ so sánh và tái sử dụng.

**Ví dụ**

Khi thiết kế miền dữ liệu: 'Danh mục thực thể dữ liệu' là Catalog; 'Ma trận thực thể–ứng dụng' là Matrix; 'Sơ đồ luồng dữ liệu' là Diagram; tất cả gộp vào Architecture Definition Document (Deliverable).

Câu hỏi thường gặpContent Framework định nghĩa những loại sản phẩm nào?

Deliverables (sản phẩm bàn giao), Artifacts (Catalog/Matrix/Diagram) và Building Blocks (ABB & SBB).

ABB và SBB khác nhau thế nào?

ABB (Architecture Building Block) là khối kiến trúc logic, độc lập công nghệ; SBB (Solution Building Block) là khối giải pháp cụ thể hiện thực hóa ABB.

Ba dạng Artifact là gì?

Catalog (danh mục thành phần), Matrix (ma trận quan hệ) và Diagram (sơ đồ trực quan).

**Mạch nối:** Đã có khung nội dung, chu trình ADM bắt đầu chạy. Slide tiếp theo đi vào giai đoạn đầu tiên — Preliminary, chuẩn bị năng lực trước khi phát triển kiến trúc.

### Preliminary Phase (Objectives) – Giai đoạn Chuẩn bị (Mục tiêu)

**Mô tả nội dung**

Hai mục tiêu: (1) Xác định Năng lực Kiến trúc mà tổ chức mong muốn; (2) Thiết lập Năng lực Kiến trúc đó.

**Diễn giải chi tiết**

Preliminary là giai đoạn 'chuẩn bị trước khi bắt đầu' — nó không phát triển kiến trúc cụ thể mà xây nền để làm kiến trúc được. Hai mục tiêu song hành: trước hết xác định tổ chức MUỐN năng lực kiến trúc ở mức nào (phạm vi, độ trưởng thành, kỳ vọng), rồi THIẾT LẬP năng lực đó (đội ngũ, quản trị, nguyên tắc, công cụ, khung được may đo). Đây là giai đoạn thường bị bỏ qua nhưng lại quyết định thành bại: nếu chưa có năng lực kiến trúc vững, mọi nỗ lực phát triển kiến trúc sau này sẽ thiếu nền tảng, thiếu quản trị và dễ tan rã.

**Ví dụ**

Một công ty lần đầu làm EA dùng Preliminary để lập một 'tổ kiến trúc' 3 người, chọn TOGAF làm khung, ban hành 10 nguyên tắc kiến trúc và mua công cụ mô hình hóa — trước khi động vào bất kỳ dự án cụ thể nào.

Câu hỏi thường gặpMục tiêu của giai đoạn Preliminary là gì?

Xác định năng lực kiến trúc mà tổ chức mong muốn, và thiết lập năng lực kiến trúc đó.

Vì sao Preliminary quan trọng?

Vì nó xây nền (đội ngũ, quản trị, nguyên tắc, công cụ) để mọi giai đoạn phát triển kiến trúc sau này có chỗ dựa; thiếu nó, EA dễ thiếu quản trị và tan rã.

**Mạch nối:** Sau khi rõ mục tiêu, slide tiếp theo liệt kê các bước cụ thể để thực hiện giai đoạn Preliminary.

### Preliminary Phase (Steps) – Giai đoạn Chuẩn bị (Các bước)

**Mô tả nội dung**

Sáu bước: (1) Khoanh vùng các tổ chức bị tác động; (2) Xác nhận khung quản trị và hỗ trợ; (3) Định nghĩa & thiết lập đội ngũ và tổ chức EA; (4) Nhận diện & thiết lập Nguyên tắc Kiến trúc; (5) May đo khung TOGAF (và các khung khác nếu có); (6) Xây chiến lược & kế hoạch triển khai cho công cụ và kỹ thuật.

**Diễn giải chi tiết**

Sáu bước Preliminary tạo thành một checklist thiết lập nền tảng. Bước 1 xác định phạm vi ảnh hưởng — những phần nào của doanh nghiệp nằm trong tầm EA. Bước 2 xác nhận các khung quản trị hiện có sẽ hỗ trợ (hoặc ràng buộc) EA. Bước 3 dựng đội ngũ và cơ cấu tổ chức kiến trúc — ai làm, báo cáo cho ai. Bước 4 ban hành Nguyên tắc Kiến trúc — những 'luật chơi' định hướng mọi quyết định sau này (sẽ được đào sâu ở Module 3). Bước 5 may đo TOGAF cho phù hợp bối cảnh (không dùng nguyên xi). Bước 6 chọn công cụ và kỹ thuật cùng kế hoạch triển khai. Hoàn thành sáu bước, tổ chức đã sẵn sàng bước vào Phase A.

**Ví dụ**

Bước 4 trong thực tế: tổ kiến trúc ban hành nguyên tắc 'Ưu tiên mua trước khi tự phát triển' và 'Dữ liệu là tài sản dùng chung' — mọi dự án sau này phải tuân theo.

Câu hỏi thường gặpSáu bước của Preliminary là gì?

Khoanh vùng tổ chức bị tác động; xác nhận khung quản trị/hỗ trợ; lập đội ngũ & tổ chức EA; thiết lập Nguyên tắc Kiến trúc; may đo TOGAF; xây chiến lược & kế hoạch cho công cụ và kỹ thuật.

'May đo' (tailor) TOGAF nghĩa là gì?

Là điều chỉnh khung TOGAF cho phù hợp với bối cảnh, quy mô và văn hóa của tổ chức, thay vì áp dụng nguyên xi toàn bộ.

**Mạch nối:** Năng lực kiến trúc đã sẵn sàng. Chu trình phát triển thực sự bắt đầu ở Phase A — nơi xác lập Tầm nhìn Kiến trúc cho sáng kiến.

### Phase A: Architecture Vision (Objectives & Steps)

DF

**Mô tả nội dung**

Mục tiêu: phát triển một tầm nhìn khát vọng cấp cao về năng lực và giá trị kinh doanh mà EA đề xuất sẽ mang lại. 11 bước gồm: lập dự án kiến trúc; nhận diện stakeholder & yêu cầu; xác nhận mục tiêu/động lực/ràng buộc; đánh giá năng lực; đánh giá mức sẵn sàng chuyển đổi; xác định phạm vi; xác nhận nguyên tắc; phát triển Tầm nhìn Kiến trúc; định nghĩa Value Proposition & KPI; nhận diện rủi ro & giảm thiểu; lập Statement of Architecture Work và xin phê duyệt.

**Diễn giải chi tiết**

Phase A là giai đoạn 'khởi động có chủ đích' của mỗi chu kỳ ADM. Nó tạo ra một tầm nhìn cấp cao, đầy khát vọng nhưng đủ cụ thể để xin phê duyệt và huy động nguồn lực. Mười một bước dẫn kiến trúc sư qua toàn bộ việc thiết lập bối cảnh: xác định ai liên quan (stakeholder) và họ quan tâm gì; làm rõ mục tiêu, động lực chiến lược và ràng buộc; đánh giá năng lực và mức sẵn sàng chuyển đổi; khoanh phạm vi; xác nhận nguyên tắc; và quan trọng nhất — phát triển bản Tầm nhìn Kiến trúc cùng đề xuất giá trị (Value Proposition) và KPI đo lường. Kết thúc bằng Statement of Architecture Work được ký duyệt — 'giấy phép' để tiếp tục. Nhiều bước ở đây (nhận diện stakeholder, xác nhận mục tiêu) mang tính điều phối và giao tiếp mạnh, nên Phase A vừa là việc thiết kế vừa là việc gắn kết con người.

**Ví dụ**

Với dự án WMS, Phase A trả lời: ai là stakeholder (CIO, trưởng SCM, quản lý kho…), tầm nhìn là gì (kho vận hành thời gian thực), giá trị đo bằng KPI nào (giảm 30% thời gian xuất kho), rủi ro gì và ai ký duyệt.

Câu hỏi thường gặpMục tiêu của Phase A là gì?

Phát triển tầm nhìn kiến trúc cấp cao, khát vọng, về năng lực và giá trị kinh doanh mà EA đề xuất sẽ mang lại.

Sản phẩm quan trọng nhất của Phase A là gì?

Bản Tầm nhìn Kiến trúc cùng Statement of Architecture Work được phê duyệt — 'giấy phép' để bắt đầu phát triển kiến trúc chi tiết.

Vì sao Phase A cần nhiều bước gắn kết stakeholder?

Vì tầm nhìn chỉ được duyệt và có nguồn lực khi các bên liên quan đồng thuận về mục tiêu, phạm vi và giá trị.

**Mạch nối:** Slide tiếp theo liệt kê cụ thể các đầu ra (outputs) mà Phase A tạo ra.

### Phase A: Architecture Vision (Outputs) – Đầu ra

**Mô tả nội dung**

Các đầu ra có thể gồm: Statement of Architecture Work (đã duyệt); Nguyên tắc/mục tiêu/động lực kinh doanh (đã duyệt); Nguyên tắc Kiến trúc; Đánh giá Năng lực; Tầm nhìn Kiến trúc; Architecture Definition Document (bản nháp); Kế hoạch Truyền thông; và Kho Kiến trúc (Architecture Repository).

**Diễn giải chi tiết**

Đầu ra của Phase A là bộ hồ sơ nền tảng cho cả chu kỳ ADM. Trung tâm là Statement of Architecture Work đã được phê duyệt — văn bản xác lập phạm vi, cách tiếp cận, nguồn lực và lịch trình của công việc kiến trúc, đóng vai trò như 'hợp đồng' nội bộ. Kèm theo là các nguyên tắc, mục tiêu và động lực kinh doanh đã được xác nhận; Nguyên tắc Kiến trúc; kết quả Đánh giá Năng lực (khoảng cách năng lực hiện tại so với yêu cầu); bản Tầm nhìn Kiến trúc; bản nháp Architecture Definition Document (tài liệu sẽ được bồi đắp qua các Phase B–D); Kế hoạch Truyền thông (đảm bảo đúng người nhận đúng thông tin); và Architecture Repository được khởi tạo để lưu trữ tài sản. Lưu ý: nhiều đầu ra ở đây là 'bản nháp' — chúng sẽ được hoàn thiện dần qua các giai đoạn sau, phản ánh tính lặp của ADM.

**Ví dụ**

Cuối Phase A, kiến trúc sư trình lãnh đạo một tập tài liệu: SoAW đã ký, tầm nhìn kiến trúc 1 trang, đánh giá năng lực, và kế hoạch truyền thông cho từng nhóm stakeholder.

Câu hỏi thường gặpĐầu ra quan trọng nhất của Phase A là gì?

Statement of Architecture Work đã được phê duyệt — văn bản xác lập phạm vi, cách tiếp cận, nguồn lực và lịch trình công việc kiến trúc.

Vì sao nhiều đầu ra Phase A là bản nháp?

Vì ADM là chu trình lặp — các tài liệu như Architecture Definition Document sẽ được bồi đắp và hoàn thiện dần qua các Phase B, C, D.

**Mạch nối:** Trong các bước của Phase A, việc hiểu đúng stakeholder là then chốt. Slide tiếp theo đi sâu vào kỹ thuật nhận diện và phân loại stakeholder qua một ví dụ WMS.

### Identify Stakeholders, Concerns & Requirements – Lưới Quyền lực/Quan tâm

**Mô tả nội dung**

Ma trận Power (Quyền lực) × Interest (Mức độ quan tâm) chia thành bốn ô: Keep Satisfied (quyền lực cao, quan tâm thấp), Key Players (cao–cao), Minimal Effort (thấp–thấp), Keep Informed (thấp–cao). Ví dụ dự án WMS: SCM Head muốn WMS vừa khít nhu cầu; đội phát triển muốn tối thiểu tùy biến; quản lý kho muốn giữ nguyên cách làm hiện tại.

**Diễn giải chi tiết**

Đây là kỹ thuật kinh điển để 'đọc bản đồ chính trị' của một sáng kiến. Lưới hai chiều xếp mỗi stakeholder theo Quyền lực (khả năng ảnh hưởng kết quả) và Mức độ Quan tâm (mức độ họ để tâm tới dự án), tạo ra bốn nhóm với chiến lược ứng xử khác nhau: Key Players (cao–cao) cần quản lý sát và tham gia chặt; Keep Satisfied (quyền lực cao, quan tâm thấp) cần giữ hài lòng, không làm phiền quá mức; Keep Informed (quyền lực thấp, quan tâm cao) cần thông tin đầy đủ để tận dụng sự nhiệt tình; Minimal Effort (thấp–thấp) chỉ cần nỗ lực tối thiểu. Ví dụ WMS còn cho thấy điều quan trọng: các stakeholder thường có mối quan tâm MÂU THUẪN nhau (SCM Head muốn tùy biến tối đa, đội dev muốn tùy biến tối thiểu, quản lý kho muốn không đổi) — và việc của kiến trúc sư là dung hòa các mối quan tâm đó.

Ví dụ ◨ có sơ đồ

Trong lưới WMS, CEO và SCM Head là Key Players (họp thường xuyên); CFO có thể là Keep Satisfied; đội phần mềm là Keep Informed — mỗi nhóm nhận một cách giao tiếp riêng.

Câu hỏi thường gặpLưới Power/Interest phân stakeholder thành mấy nhóm?

Bốn: Key Players (cao–cao), Keep Satisfied (quyền lực cao, quan tâm thấp), Keep Informed (quyền lực thấp, quan tâm cao) và Minimal Effort (thấp–thấp).

Nên ứng xử với Key Players thế nào?

Quản lý sát sao và cho họ tham gia chặt chẽ, vì họ vừa có quyền lực vừa quan tâm cao tới dự án.

Bài học từ ví dụ WMS là gì?

Các stakeholder thường có mối quan tâm mâu thuẫn nhau; nhiệm vụ của kiến trúc sư là nhận diện và dung hòa các mối quan tâm đó.

**Mạch nối:** Hiểu stakeholder rồi, bước tiếp theo trong Phase A là làm rõ mục tiêu và ràng buộc kinh doanh mà kiến trúc phải phục vụ.

### Confirm Business Goals, Drivers & Constraints – Mục tiêu, Động lực & Ràng buộc

DF

**Mô tả nội dung**

Ba việc: (1) Nhận diện mục tiêu kinh doanh và động lực chiến lược của tổ chức; (2) Nếu đã có sẵn, đảm bảo định nghĩa hiện tại còn đúng và làm rõ chỗ mơ hồ; (3) Định nghĩa các ràng buộc phải xử lý, gồm ràng buộc toàn doanh nghiệp và ràng buộc riêng của dự án.

**Diễn giải chi tiết**

Bước này neo kiến trúc vào thực tế kinh doanh và giới hạn thực tế. Mục tiêu (goals) và động lực (drivers) trả lời câu hỏi 'kiến trúc này phục vụ điều gì' — nếu không rõ, kiến trúc dễ trở thành bài tập kỹ thuật vô định hướng. Khi mục tiêu đã tồn tại, kiến trúc sư không tạo mới mà xác nhận chúng còn hiệu lực và gỡ bỏ mơ hồ. Đồng thời phải làm rõ các ràng buộc (constraints) — cả ràng buộc cấp doanh nghiệp (ngân sách, tuân thủ pháp lý, tiêu chuẩn) lẫn ràng buộc riêng dự án (thời hạn, công nghệ bắt buộc). Ràng buộc không phải là kẻ thù mà là điều kiện biên giúp kiến trúc thực tế và khả thi.

**Ví dụ**

Mục tiêu 'tăng 20% doanh thu online', động lực 'cạnh tranh từ sàn TMĐT', ràng buộc 'phải tuân thủ luật bảo vệ dữ liệu cá nhân và ngân sách 2 tỷ' — ba yếu tố này định hình mọi lựa chọn kiến trúc sau đó.

Câu hỏi thường gặpBa việc cần làm ở bước này là gì?

Nhận diện mục tiêu & động lực chiến lược; xác nhận định nghĩa hiện có còn đúng và làm rõ mơ hồ; định nghĩa các ràng buộc cấp doanh nghiệp và cấp dự án.

Vì sao phải làm rõ ràng buộc?

Vì ràng buộc là điều kiện biên (ngân sách, pháp lý, thời hạn, công nghệ) giúp kiến trúc thực tế và khả thi thay vì lý tưởng hóa.

**Mạch nối:** Biết mục tiêu và ràng buộc rồi, kiến trúc sư cần đánh giá xem doanh nghiệp có đủ năng lực để đạt mục tiêu không. Đó là nội dung slide tiếp theo.

### Evaluate Business Capabilities – Đánh giá Năng lực Nghiệp vụ

**Mô tả nội dung**

Nhận diện các năng lực nghiệp vụ cần có để hành động theo ưu tiên chiến lược, rồi tìm khoảng trống (gaps) theo nhiều miền: khoảng trống nghiệp vụ (con người, quy trình, công cụ, thông tin, đo lường, tài chính, cơ sở vật chất), khoảng trống dữ liệu (dữ liệu không đủ mới, không đúng chỗ, không có khi cần…), và các ứng dụng/công nghệ bị tác động, loại bỏ hoặc tạo mới.

**Diễn giải chi tiết**

Đánh giá năng lực là bước xác định 'doanh nghiệp còn thiếu gì' để đạt mục tiêu. Trước hết nhận diện các năng lực nghiệp vụ cần thiết để hiện thực hóa ưu tiên chiến lược, rồi so với hiện trạng để lộ ra khoảng trống. Các khoảng trống được phân loại có hệ thống: ở miền nghiệp vụ (thiếu kỹ năng người, quy trình kém hiệu quả, công cụ trùng lắp/thiếu, thiếu thông tin, thiếu đo lường, thiếu ngân sách, thiếu cơ sở vật chất); ở miền dữ liệu (dữ liệu cũ, sai vị trí, sai loại, không sẵn khi cần, chưa tạo, chưa dùng, thiếu quan hệ dữ liệu); và ở miền ứng dụng/công nghệ (những gì bị ảnh hưởng, phải bỏ hoặc phải tạo mới). Việc phân loại chi tiết này giúp không bỏ sót bất kỳ loại khoảng trống nào khi lập kế hoạch.

**Ví dụ**

Để bán hàng đa kênh, doanh nghiệp phát hiện khoảng trống: thiếu nhân sự phân tích dữ liệu (people), quy trình đổi trả thủ công (process), thiếu dữ liệu tồn kho thời gian thực (data) — mỗi khoảng trống thành một hạng mục cần giải quyết.

Câu hỏi thường gặpĐánh giá năng lực nghiệp vụ nhằm mục đích gì?

Nhận diện các năng lực nghiệp vụ cần có để hành động theo ưu tiên chiến lược, và tìm khoảng trống so với hiện trạng.

Khoảng trống được phân loại theo những miền nào?

Miền nghiệp vụ (con người, quy trình, công cụ, thông tin, đo lường, tài chính, cơ sở vật chất), miền dữ liệu, và ứng dụng/công nghệ bị tác động/loại bỏ/tạo mới.

**Mạch nối:** Biết khoảng trống năng lực, câu hỏi kế tiếp là doanh nghiệp có SẴN SÀNG cho sự chuyển đổi không. Slide tiếp theo trình bày đánh giá mức sẵn sàng chuyển đổi.

### Assess Readiness for Business Transformation – Đánh giá Mức sẵn sàng

DF

**Mô tả nội dung**

Các hoạt động khuyến nghị: (1) Xác định các yếu tố sẵn sàng ảnh hưởng tổ chức; (2) Trình bày các yếu tố đó qua mô hình trưởng thành (maturity model); (3) Đánh giá và cho điểm mức sẵn sàng; (4) Đánh giá rủi ro cho từng yếu tố và xác định hành động cải thiện; (5) Đưa các hành động này vào Kế hoạch Triển khai & Di trú ở Phase E và F.

**Diễn giải chi tiết**

Chuyển đổi thất bại thường không vì công nghệ kém mà vì tổ chức chưa sẵn sàng. Bước này đánh giá 'sức khỏe chuyển đổi' một cách có hệ thống: xác định các yếu tố sẵn sàng (như sự ủng hộ của lãnh đạo, năng lực đội ngũ, văn hóa thay đổi, ngân sách), rồi dùng mô hình trưởng thành để định vị mỗi yếu tố đang ở mức nào. Sau đó cho điểm, đánh giá rủi ro của từng yếu tố và đề ra hành động cải thiện. Điểm quan trọng: các hành động cải thiện này không nằm im trên giấy mà được đưa thẳng vào kế hoạch triển khai ở Phase E và F — biến đánh giá thành hành động thực. Đây là cầu nối giữa 'phân tích' và 'kế hoạch'.

**Ví dụ**

Đánh giá cho thấy yếu tố 'văn hóa chấp nhận thay đổi' ở mức thấp và rủi ro cao; hành động cải thiện — chương trình quản lý thay đổi và đào tạo — được đưa vào kế hoạch Phase F.

Câu hỏi thường gặpĐánh giá mức sẵn sàng gồm những hoạt động nào?

Xác định yếu tố sẵn sàng; trình bày qua mô hình trưởng thành; đánh giá và cho điểm; đánh giá rủi ro & xác định hành động cải thiện; đưa hành động vào kế hoạch Phase E và F.

Vì sao đánh giá mức sẵn sàng quan trọng?

Vì chuyển đổi thường thất bại do tổ chức chưa sẵn sàng (lãnh đạo, năng lực, văn hóa) chứ không phải do công nghệ — nên phải nhận diện và xử lý sớm.

**Mạch nối:** Sau khi hiểu năng lực và mức sẵn sàng, kiến trúc sư cần khoanh vùng công việc cho rõ. Slide tiếp theo bàn về việc Định nghĩa Phạm vi.

### Define Scope – Định nghĩa Phạm vi

**Mô tả nội dung**

Phạm vi tự 'phình ra' (scope creep) khi thiếu kiểm soát; nhưng nghĩ rằng phạm vi không đổi chút nào là ngây thơ. Không định nghĩa được hoàn hảo không có nghĩa là không nên cố. Trong EA, phạm vi được kiểm soát qua bốn chiều: Breadth (độ rộng phủ), Depth (độ sâu chi tiết), Time (khung thời gian của tầm nhìn), và Architecture Domain (Business, Data, Application, Technology…).

**Diễn giải chi tiết**

Định nghĩa phạm vi là nghệ thuật cân bằng giữa 'quá rộng đến mức không làm nổi' và 'quá hẹp đến mức vô nghĩa'. Slide thừa nhận một thực tế: phạm vi luôn có xu hướng phình ra (scope creep) nếu không kiểm soát, nhưng cũng không thể cố định tuyệt đối — nên cứ phải cố khoanh vùng dù không hoàn hảo. EA kiểm soát phạm vi qua bốn chiều rõ ràng: Breadth (kiến trúc phủ bao nhiêu phần của doanh nghiệp), Depth (đi sâu tới mức chi tiết nào), Time (tầm nhìn cho khoảng thời gian bao lâu), và Architecture Domain (bao gồm những miền BDAT nào). Bốn chiều này biến 'phạm vi' từ một khái niệm mơ hồ thành các quyết định cụ thể, có thể thảo luận và thống nhất.

**Ví dụ**

Phạm vi một dự án EA: Breadth = khối vận hành kho; Depth = tới mức quy trình con; Time = tầm nhìn 3 năm; Domain = Business + Data + Application (chưa gồm Technology chi tiết) — bốn chiều được chốt rõ để tránh phình việc.

Câu hỏi thường gặpBốn chiều kiểm soát phạm vi trong EA là gì?

Breadth (độ rộng phủ), Depth (độ sâu chi tiết), Time (khung thời gian tầm nhìn) và Architecture Domain (các miền BDAT được bao gồm).

'Scope creep' là gì?

Là hiện tượng phạm vi tự phình ra ngoài dự kiến khi thiếu kiểm soát — cần được quản lý dù không thể định nghĩa phạm vi một cách hoàn hảo.

**Mạch nối:** Có phạm vi rồi, kiến trúc sư xác nhận nguyên tắc và phát triển tầm nhìn. Slide tiếp theo gộp ba việc: xác nhận nguyên tắc, phát triển Tầm nhìn và định nghĩa giá trị/KPI.

### Confirm Principles & Develop Architecture Vision

DF

**Mô tả nội dung**

Ba việc nối tiếp: (1) Xác nhận & làm rõ Nguyên tắc Kiến trúc, gồm cả Nguyên tắc Kinh doanh; (2) Phát triển Tầm nhìn Kiến trúc; (3) Định nghĩa Đề xuất Giá trị của Kiến trúc Mục tiêu và các KPI.

**Diễn giải chi tiết**

Ba việc này biến bối cảnh đã thu thập thành một tầm nhìn có định hướng và đo được. Trước hết, xác nhận và làm rõ Nguyên tắc Kiến trúc (bao gồm cả nguyên tắc kinh doanh) — đây là 'kim chỉ nam' loại bỏ tính chủ quan khỏi các quyết định sau này. Tiếp đó phát triển Tầm nhìn Kiến trúc — bức tranh khát vọng về trạng thái tương lai. Cuối cùng, định nghĩa Đề xuất Giá trị (Value Proposition) và các KPI cho kiến trúc mục tiêu — trả lời câu hỏi 'kiến trúc này mang lại giá trị gì và đo bằng gì'. Bộ ba nguyên tắc + tầm nhìn + KPI này bảo đảm tầm nhìn không chỉ đẹp mà còn có định hướng rõ và thước đo cụ thể.

**Ví dụ**

Nguyên tắc 'dữ liệu dùng chung' + tầm nhìn 'kho thời gian thực' + KPI 'giảm 30% thời gian xuất kho' — ba yếu tố cùng định hình một tầm nhìn vừa có định hướng vừa đo được.

Câu hỏi thường gặpBa việc trong bước này là gì?

Xác nhận & làm rõ Nguyên tắc Kiến trúc (gồm nguyên tắc kinh doanh); phát triển Tầm nhìn Kiến trúc; định nghĩa Đề xuất Giá trị và KPI của kiến trúc mục tiêu.

Vì sao cần Nguyên tắc Kiến trúc trước khi phát triển tầm nhìn?

Vì nguyên tắc là kim chỉ nam loại bỏ tính chủ quan, giúp mọi quyết định trong tầm nhìn nhất quán và có căn cứ.

**Mạch nối:** Trong ba việc trên, việc định nghĩa giá trị và KPI cần được làm rõ thêm. Slide tiếp theo đào sâu vào Value Proposition và KPI của kiến trúc mục tiêu.

### Define Target Architecture Value Propositions & KPIs

DF

**Mô tả nội dung**

KPI = 'Key Performance Indicators' (Chỉ số Hiệu suất Then chốt). Bắt đầu bằng phần trăm hoàn thành vẽ theo thời gian còn lại. Tạo một dashboard KPI mà stakeholder có thể xem bất cứ lúc nào. Giữ nó luôn cập nhật để mọi người được thông tin đầy đủ.

**Diễn giải chi tiết**

KPI biến giá trị kỳ vọng từ lời hứa thành con số theo dõi được. Cách làm thực dụng được gợi ý: khởi đầu đơn giản bằng chỉ số 'phần trăm hoàn thành so với thời gian còn lại' để thấy tiến độ; rồi dựng một dashboard KPI mở, nơi stakeholder tự xem bất cứ lúc nào — sự minh bạch này xây niềm tin và giảm nhu cầu báo cáo thủ công. Điều kiện sống còn của dashboard là được cập nhật liên tục; một dashboard cũ còn tệ hơn không có, vì nó tạo cảm giác an tâm giả. Value Proposition trả lời 'vì sao đáng đầu tư', còn KPI trả lời 'làm sao biết đang thành công' — hai mặt của cùng một cam kết giá trị.

**Ví dụ**

Dashboard hiển thị: tiến độ triển khai 60%, thời gian xuất kho đã giảm 18% (mục tiêu 30%), tỷ lệ đơn xử lý tự động 75% — lãnh đạo mở xem bất cứ lúc nào thay vì chờ báo cáo tháng.

Câu hỏi thường gặpKPI là gì?

Key Performance Indicators — Chỉ số Hiệu suất Then chốt, dùng để đo mức độ đạt được giá trị kỳ vọng của kiến trúc.

Nên trình bày KPI thế nào?

Qua một dashboard mà stakeholder xem được bất cứ lúc nào, luôn được cập nhật, giúp mọi người nắm thông tin đầy đủ và minh bạch.

**Mạch nối:** Giá trị và KPI đã rõ, nhưng mọi chuyển đổi đều có rủi ro. Slide tiếp theo trình bày cách nhận diện và giảm thiểu rủi ro chuyển đổi kinh doanh.

### Identify Business Transformation Risks & Mitigation

**Mô tả nội dung**

Phân loại rủi ro theo hai trục. Mức tác động: Catastrophic (thảm khốc, có thể phá sản), Critical (nghiêm trọng, mất năng suất, không ROI), Marginal (nhỏ, giảm ROI), Negligible (không đáng kể). Tần suất: Frequent, Likely, Occasional, Seldom, Unlikely. Kết hợp thành mức rủi ro: Extremely High (E), High (H), Moderate (M), Low (L).

**Diễn giải chi tiết**

Quản lý rủi ro chuyển đổi dựa trên một ma trận hai chiều kinh điển: Mức tác động × Tần suất xảy ra. Trục tác động đi từ Negligible (ảnh hưởng tối thiểu) đến Catastrophic (tổn thất tài chính tới mức phá sản), qua Marginal và Critical. Trục tần suất đi từ Unlikely (khó xảy ra) đến Frequent (xảy ra rất thường xuyên). Kết hợp hai trục cho ra bốn mức rủi ro tổng hợp: Extremely High (E — gần như chắc thất bại với hậu quả nặng), High (H — thất bại đáng kể một phần), Moderate (M — thất bại đáng chú ý đe dọa một số mục tiêu), Low (L — một số mục tiêu không hoàn toàn thành công). Ma trận này giúp ưu tiên nguồn lực giảm thiểu: dồn sức vào các rủi ro E và H trước, chấp nhận theo dõi các rủi ro L.

**Ví dụ**

Rủi ro 'nhà cung cấp ERP phá sản giữa dự án' — tác động Critical, tần suất Seldom → mức High; cần kế hoạch dự phòng nhà cung cấp thay thế.

Câu hỏi thường gặpRủi ro được phân loại theo mấy trục?

Hai trục: Mức tác động (Negligible → Catastrophic) và Tần suất (Unlikely → Frequent), kết hợp thành mức rủi ro E/H/M/L.

Bốn mức rủi ro tổng hợp là gì?

Extremely High (E), High (H), Moderate (M) và Low (L).

Dùng ma trận rủi ro để làm gì?

Để ưu tiên nguồn lực giảm thiểu — tập trung vào rủi ro E và H trước, theo dõi các rủi ro L.

**Mạch nối:** Đã nhận diện rủi ro và giảm thiểu, Phase A đi tới bước cuối: gói tất cả vào một tuyên bố công việc và xin phê duyệt. Đó là nội dung slide tiếp theo.

### Develop Statement of Architecture Work; Secure Approval

DF

**Mô tả nội dung**

Đến giờ ta đã có bức tranh rõ ràng về cả dự án lẫn năng lực của doanh nghiệp, kèm kế hoạch giảm thiểu các rủi ro quan trọng. Giờ có thể ước lượng tác động lên con người và quy trình, quyết định cần nguồn lực gì — và đã đến lúc trình lãnh đạo ký duyệt.

**Diễn giải chi tiết**

Statement of Architecture Work (SoAW) là sản phẩm gói lại toàn bộ Phase A thành một văn bản để xin phê duyệt. Nó tổng hợp mọi thứ đã làm: bức tranh rõ về dự án và năng lực doanh nghiệp, kế hoạch giảm thiểu rủi ro trọng yếu, ước lượng tác động lên con người và quy trình, và các nguồn lực cần thiết. SoAW đóng vai trò như một 'hợp đồng' nội bộ — khi lãnh đạo ký, họ cam kết nguồn lực và trao quyền cho công việc kiến trúc tiếp tục. Bước ký duyệt này rất quan trọng về mặt điều phối: nó tạo ra sự cam kết chính thức và trách nhiệm chung, biến kiến trúc từ đề xuất thành công việc được ủy quyền.

**Ví dụ**

Kiến trúc sư trình SoAW cho ban giám đốc: 'dự án WMS, tầm nhìn kho thời gian thực, cần 5 người 6 tháng, ngân sách 2 tỷ, rủi ro chính đã có phương án' — lãnh đạo ký, dự án chính thức khởi động.

Câu hỏi thường gặpStatement of Architecture Work là gì?

Văn bản gói lại toàn bộ Phase A — phạm vi, cách tiếp cận, nguồn lực, rủi ro và tác động — để trình lãnh đạo phê duyệt, đóng vai trò như 'hợp đồng' nội bộ.

Vì sao cần được ký duyệt?

Vì chữ ký của lãnh đạo tạo ra cam kết nguồn lực chính thức và trao quyền cho công việc kiến trúc tiếp tục sang các Phase B–H.

**Mạch nối:** Phase A hoàn tất với tầm nhìn đã được duyệt. Chu trình bước vào Phase B — nơi phát triển kiến trúc nghiệp vụ chi tiết đầu tiên.

### Phase B: Business Architecture (Objectives)

**Mô tả nội dung**

Hai mục tiêu: (1) Phát triển Kiến trúc Nghiệp vụ Mục tiêu mô tả cách doanh nghiệp cần vận hành để đạt mục tiêu kinh doanh và đáp ứng động lực chiến lược trong Tầm nhìn, theo cách xử lý được Statement of Architecture Work và mối quan tâm của stakeholder; (2) Nhận diện các thành phần lộ trình kiến trúc ứng viên dựa trên khoảng cách giữa Kiến trúc Nghiệp vụ Baseline và Target.

**Diễn giải chi tiết**

Phase B là giai đoạn đầu tiên phát triển kiến trúc chi tiết, và nó bắt đầu từ nghiệp vụ — vì mọi thứ khác (dữ liệu, ứng dụng, công nghệ) đều phải phục vụ nghiệp vụ. Mục tiêu đầu là xây Kiến trúc Nghiệp vụ Mục tiêu: mô tả doanh nghiệp CẦN vận hành thế nào (năng lực, quy trình, tổ chức, dòng giá trị) để đạt mục tiêu trong Tầm nhìn, đồng thời giải quyết mối quan tâm của stakeholder. Mục tiêu thứ hai là so sánh Baseline (hiện tại) với Target (mục tiêu) để lộ ra khoảng cách, từ đó nhận diện các 'thành phần lộ trình ứng viên' — những việc cần làm sẽ đưa vào roadmap. Đây là lần đầu 'sợi chỉ vàng' Baseline → Gap → Target được áp dụng vào một miền cụ thể.

**Ví dụ**

Phase B của dự án WMS mô tả quy trình kho mục tiêu (nhập–xuất–kiểm kê tự động), so với quy trình thủ công hiện tại, và liệt kê khoảng cách như 'thiếu quy trình kiểm kê thời gian thực' làm ứng viên roadmap.

Câu hỏi thường gặpMục tiêu của Phase B là gì?

Phát triển Kiến trúc Nghiệp vụ Mục tiêu (cách doanh nghiệp cần vận hành để đạt mục tiêu) và nhận diện thành phần lộ trình dựa trên khoảng cách Baseline–Target.

Vì sao ADM bắt đầu phát triển chi tiết từ nghiệp vụ?

Vì dữ liệu, ứng dụng và công nghệ đều phải phục vụ nghiệp vụ — nên phải rõ nghiệp vụ mục tiêu trước.

**Mạch nối:** Sau mục tiêu, slide tiếp theo liệt kê các đầu ra cụ thể của Phase B — những thành phần kiến trúc nghiệp vụ cho lộ trình.

### Phase B: Business Architecture (Outputs)

**Mô tả nội dung**

Đầu ra là các thành phần Kiến trúc Nghiệp vụ của một Lộ trình Kiến trúc — kèm danh sách gợi ý các thành phần kiến trúc (architecture components) cần tạo ra trong miền nghiệp vụ.

**Diễn giải chi tiết**

Đầu ra của Phase B là bộ thành phần mô tả kiến trúc nghiệp vụ, sẽ trở thành các mảnh ghép của Lộ trình Kiến trúc tổng thể. Chúng thường gồm: bản mô tả Kiến trúc Nghiệp vụ Baseline và Target đã hoàn thiện; kết quả phân tích khoảng cách; các thành phần lộ trình ứng viên; và phần cập nhật vào Architecture Definition Document cùng Architecture Requirements Specification. Danh sách gợi ý các thành phần (như Bản đồ Năng lực, Danh mục Quy trình, Mô hình Tổ chức, Bản đồ Dòng giá trị…) giúp kiến trúc sư không bỏ sót tạo phẩm quan trọng. Điểm cần nhớ: các đầu ra này là 'nguyên liệu' cho Phase E khi lắp ráp lộ trình tổng thể — nên phải rõ ràng và có thể ưu tiên.

**Ví dụ**

Đầu ra Phase B gồm: Bản đồ năng lực nghiệp vụ, danh mục quy trình mục tiêu, kết quả gap analysis, và 5 thành phần lộ trình ứng viên như 'chuẩn hóa quy trình kiểm kê'.

Câu hỏi thường gặpĐầu ra chính của Phase B là gì?

Các thành phần Kiến trúc Nghiệp vụ của Lộ trình Kiến trúc — mô tả Baseline/Target, kết quả gap analysis và các thành phần lộ trình ứng viên.

Các đầu ra Phase B dùng cho giai đoạn nào?

Chúng là nguyên liệu cho Phase E khi lắp ráp Lộ trình Kiến trúc tổng thể.

**Mạch nối:** Biết đầu ra rồi, slide tiếp theo trình bày các bước cụ thể để tạo ra chúng — quy trình 9 bước của Phase B.

### Phase B: Business Architecture (Steps)

**Mô tả nội dung**

Chín bước (mẫu chung cho các phase kiến trúc B–D): (1) Chọn mô hình tham chiếu, viewpoint & công cụ; (2) Phát triển mô tả Kiến trúc Baseline; (3) Phát triển mô tả Kiến trúc Target; (4) Phân tích khoảng cách; (5) Định nghĩa thành phần lộ trình ứng viên; (6) Giải quyết tác động xuyên Architecture Landscape; (7) Rà soát chính thức với stakeholder; (8) Hoàn thiện Kiến trúc Nghiệp vụ; (9) Tạo/Cập nhật Architecture Definition Document.

**Diễn giải chi tiết**

Chín bước này là 'khuôn mẫu' được lặp lại gần như giống nhau cho các Phase B, C và D — một khi thuộc, kiến trúc sư có thể áp dụng cho mọi miền. Mạch logic: chọn công cụ và góc nhìn phù hợp → mô tả hiện trạng (Baseline) → mô tả mục tiêu (Target) → so sánh để tìm khoảng cách (gap analysis) → biến khoảng cách thành thành phần lộ trình → kiểm tra tác động lan tỏa sang các phần kiến trúc khác (Architecture Landscape) → rà soát với stakeholder để đồng thuận → hoàn thiện → ghi vào tài liệu. Việc dùng chung một khuôn 9 bước cho ba miền BDAT giúp quy trình nhất quán và dễ học.

**Ví dụ**

Áp khuôn 9 bước cho miền nghiệp vụ: mô tả quy trình kho hiện tại (baseline), quy trình mục tiêu (target), tìm khoảng cách, chốt với trưởng kho (stakeholder review), rồi ghi vào ADD.

Câu hỏi thường gặpChín bước của Phase B là gì?

Chọn mô hình/viewpoint/công cụ; mô tả Baseline; mô tả Target; phân tích khoảng cách; định nghĩa thành phần lộ trình; giải quyết tác động xuyên landscape; rà soát stakeholder; hoàn thiện; cập nhật ADD.

Vì sao khuôn 9 bước này quan trọng?

Vì nó được lặp lại gần như giống nhau cho Phase B, C và D — thuộc một lần, áp dụng cho mọi miền, giúp quy trình nhất quán.

**Mạch nối:** Trước khi đi tiếp, cần làm rõ một hiểu lầm phổ biến. Slide tiếp theo giải thích 'Business Architecture' thực sự nghĩa là gì.

### What 'Business Architecture' Means – Ý nghĩa thực sự

**Mô tả nội dung**

Không phải 'tầng nghiệp vụ' (Business Layer) mà là kiến trúc CỦA doanh nghiệp. Ta muốn mô hình hóa trạng thái doanh nghiệp như hiện tại, và như sẽ trở thành sau khi đạt mục tiêu dự án, rồi tìm ra sự khác biệt giữa hai trạng thái. Trừ khi đây là lần đầu, các vòng lặp trước sẽ cho ta điểm khởi đầu.

**Diễn giải chi tiết**

Đây là một điểm dễ hiểu sai cần làm rõ: 'Business Architecture' KHÔNG phải là một tầng kỹ thuật trong sơ đồ hệ thống, mà là kiến trúc CỦA chính doanh nghiệp — cách doanh nghiệp được cấu trúc và vận hành. Mục đích của nó rất thực dụng: mô hình hóa doanh nghiệp ở trạng thái hiện tại (as-is) và trạng thái sau khi đạt mục tiêu (to-be), rồi xác định khác biệt — chính khác biệt đó là thứ dự án phải tạo ra. Một lưu ý thực tế: nếu đã có các vòng lặp ADM trước, kiến trúc sư không bắt đầu từ con số 0 mà kế thừa mô hình cũ làm điểm xuất phát — thể hiện tính lặp và tích lũy của EA.

**Ví dụ**

Business Architecture không phải 'sơ đồ phần mềm tầng nghiệp vụ' mà là mô hình 'công ty vận hành thế nào hôm nay vs sau khi số hóa kho' — khoảng cách giữa hai mô hình chính là việc cần làm.

Câu hỏi thường gặpBusiness Architecture có phải là 'tầng nghiệp vụ' của hệ thống không?

Không — nó là kiến trúc CỦA doanh nghiệp (cách doanh nghiệp được cấu trúc và vận hành), không phải một tầng kỹ thuật trong sơ đồ phần mềm.

Business Architecture mô hình hóa những gì?

Trạng thái doanh nghiệp hiện tại (as-is) và trạng thái mục tiêu (to-be), rồi xác định khác biệt giữa chúng — chính là việc dự án phải làm.

**Mạch nối:** Hiểu đúng bản chất rồi, slide tiếp theo đi sâu vào cặp đôi cốt lõi của Phase B: kiến trúc mục tiêu và phân tích khoảng cách.

### Target Architecture & Gap Analysis – Kiến trúc Mục tiêu & Phân tích Khoảng cách

**Mô tả nội dung**

Với con người, quy trình, cơ sở vật chất và năng lực: bạn đã mô hình kiến trúc hiện tại, giờ mô hình kiến trúc tương lai. Khoảng cách #1 mà TOGAF chỉ ra là 'KHÔNG GIẢI QUYẾT MỐI QUAN TÂM CỦA STAKEHOLDER'. Nguồn khoảng cách gồm: People, Processes, Tools, Financial, Information, Measurement.

**Diễn giải chi tiết**

Phân tích khoảng cách là kỹ thuật trung tâm của mọi phase kiến trúc: đặt mô hình hiện tại cạnh mô hình tương lai và tìm ra sự khác biệt cần lấp. Slide nhấn mạnh một cảnh báo đắt giá từ TOGAF: khoảng cách nguy hiểm nhất (#1) không phải là thiếu công nghệ, mà là 'không giải quyết mối quan tâm của stakeholder' — một kiến trúc kỹ thuật hoàn hảo nhưng bỏ qua điều stakeholder cần vẫn là thất bại. Các nguồn khoảng cách được phân loại rõ để rà soát có hệ thống: People (thiếu người/kỹ năng), Processes (quy trình kém), Tools (công cụ thiếu/trùng), Financial (thiếu ngân sách), Information (thiếu thông tin), Measurement (thiếu đo lường). Việc liệt kê đủ các nguồn giúp không bỏ sót khoảng cách nào.

**Ví dụ**

Gap analysis kho hàng: hiện tại kiểm kê thủ công cuối ngày, mục tiêu kiểm kê tự động thời gian thực → khoảng cách gồm thiếu thiết bị quét (Tools), thiếu quy trình mới (Processes), thiếu nhân sự vận hành (People).

Câu hỏi thường gặpKhoảng cách #1 theo TOGAF là gì?

'Không giải quyết mối quan tâm của stakeholder' — nguy hiểm hơn cả thiếu công nghệ, vì một kiến trúc bỏ qua nhu cầu stakeholder vẫn thất bại.

Các nguồn khoảng cách gồm những gì?

People, Processes, Tools, Financial, Information và Measurement.

**Mạch nối:** Trong nghiệp vụ, khái niệm 'năng lực' (capability) là trung tâm. Slide tiếp theo trình bày các thành phần và quan hệ của Năng lực Nghiệp vụ.

### Business Capability Elements & Relationships

**Mô tả nội dung**

Trình bày các thành phần cấu thành một Năng lực Nghiệp vụ (Business Capability) và quan hệ giữa chúng — như năng lực gắn với quy trình, thông tin, vai trò/con người, công cụ và được đo bằng các chỉ số hiệu suất.

**Diễn giải chi tiết**

Năng lực nghiệp vụ (business capability) là 'viên gạch' trung tâm của kiến trúc nghiệp vụ hiện đại — nó mô tả doanh nghiệp CÓ KHẢ NĂNG LÀM GÌ (ổn định) thay vì LÀM THẾ NÀO (dễ đổi). Một năng lực không đứng một mình mà được cấu thành và liên kết bởi nhiều yếu tố: các quy trình hiện thực hóa nó, thông tin/dữ liệu nó cần, vai trò và con người thực hiện, công cụ/ứng dụng hỗ trợ, và các chỉ số đo hiệu suất. Hiểu các thành phần và quan hệ này cho phép kiến trúc sư phân tích một năng lực toàn diện: muốn nâng cấp năng lực 'quản lý tồn kho' thì phải xem xét đồng thời quy trình, dữ liệu, con người, công cụ và thước đo của nó — chứ không chỉ mua một phần mềm mới.

Ví dụ ◨ có sơ đồ

Năng lực 'Quản lý đơn hàng' gồm: quy trình xử lý đơn, dữ liệu đơn hàng, vai trò nhân viên bán hàng, ứng dụng OMS, và KPI 'thời gian xử lý đơn' — muốn cải thiện năng lực phải nhìn cả năm yếu tố.

Câu hỏi thường gặpBusiness Capability là gì?

Là mô tả doanh nghiệp CÓ KHẢ NĂNG LÀM GÌ (ổn định theo thời gian), khác với quy trình mô tả LÀM THẾ NÀO (dễ thay đổi).

Một năng lực nghiệp vụ gồm những thành phần nào?

Các quy trình hiện thực hóa nó, thông tin/dữ liệu cần, vai trò/con người, công cụ/ứng dụng hỗ trợ và các chỉ số đo hiệu suất.

**Mạch nối:** Sau khi biết cấu thành năng lực, slide tiếp theo bàn về một điểm quan trọng: hiểu đúng bản chất của năng lực và mối quan hệ giữa nghiệp vụ với IT.

### Understanding Capability – Hiểu đúng về Năng lực

**Mô tả nội dung**

Năng lực do nghiệp vụ dẫn dắt (business-driven) cho kết quả khác với năng lực do công nghệ dẫn dắt (technology-driven). Tuy nhiên, nếu không gắn kết với IT, kiến trúc nghiệp vụ có nguy cơ cao thất bại trong việc hiện thực hóa các mục tiêu chiến lược.

**Diễn giải chi tiết**

Slide này nêu một sự cân bằng tinh tế. Một mặt, năng lực do nghiệp vụ dẫn dắt cho kết quả khác hẳn năng lực do công nghệ dẫn dắt — nếu để công nghệ dẫn dắt, ta dễ rơi vào bẫy 'có búa nên thấy gì cũng là đinh', mua công nghệ rồi mới tìm chỗ dùng. Vì vậy nghiệp vụ nên dẫn dắt: xác định cần năng lực gì trước, rồi mới chọn công nghệ. Mặt khác, slide cảnh báo chiều ngược lại: nếu kiến trúc nghiệp vụ KHÔNG gắn kết với IT, nó có nguy cơ cao thất bại trong việc đạt mục tiêu chiến lược — vì trong thời đại số, hầu hết năng lực nghiệp vụ đều cần IT để hiện thực hóa. Kết luận: nghiệp vụ dẫn dắt định hướng, nhưng phải luôn gắn chặt với IT — hai bên là đối tác, không phải chủ–tớ.

**Ví dụ**

Nghiệp vụ xác định cần năng lực 'giao hàng trong 2 giờ' (business-driven), rồi IT chọn công nghệ định tuyến & theo dõi phù hợp — thay vì IT mua phần mềm rồi ép nghiệp vụ dùng.

Câu hỏi thường gặpNăng lực do nghiệp vụ dẫn dắt khác gì do công nghệ dẫn dắt?

Business-driven xác định cần năng lực gì trước rồi mới chọn công nghệ; technology-driven dễ mua công nghệ trước rồi tìm chỗ dùng, cho kết quả khác nhau.

Vì sao kiến trúc nghiệp vụ vẫn phải gắn với IT?

Vì không gắn kết với IT, kiến trúc nghiệp vụ có nguy cơ cao thất bại trong hiện thực hóa mục tiêu chiến lược — trong thời đại số hầu hết năng lực đều cần IT.

**Mạch nối:** Hiểu năng lực rồi, slide tiếp theo trình bày cách tiếp cận Phase B qua các công cụ trực quan như Bản đồ Năng lực và Heatmap.

### Phase B: Business Architecture (Approach) – Capability Map & Heatmap

**Mô tả nội dung**

Bản đồ năng lực nghiệp vụ chia ba tầng: Strategic (Business/Market Planning, Partner/Capital/Policy/Government Relations Management), Core (Account, Product, Distribution, Customer, Channel, Agent Management) và Supporting (Financial, HR, Procurement, IT, Training, Operations Management). Kèm kỹ thuật: Heatmap, ánh xạ Value stream stage → Capability, Information map, và các kỹ thuật mô hình hóa (Business Process Model, Use-Case Model, Logical Model).

**Diễn giải chi tiết**

Slide này trình bày bộ công cụ trực quan chủ lực của Phase B. Bản đồ Năng lực (Capability Map) sắp xếp mọi năng lực nghiệp vụ thành ba tầng: Strategic (các năng lực định hướng như hoạch định kinh doanh, quản lý đối tác, chính sách), Core (các năng lực tạo giá trị trực tiếp như quản lý khách hàng, sản phẩm, kênh phân phối) và Supporting (các năng lực hỗ trợ như tài chính, nhân sự, IT, mua sắm). Trên bản đồ này, kỹ thuật Heatmap tô màu để làm nổi các năng lực cần đầu tư/cải thiện (thường đỏ = yếu/ưu tiên cao). Ngoài ra còn có ánh xạ Value Stream → Capability (nối dòng giá trị với năng lực), Information Map, và các kỹ thuật mô hình hóa chi tiết (quy trình, use-case, mô hình logic). Bộ công cụ này giúp biến kiến trúc nghiệp vụ từ khái niệm thành hình ảnh dễ thảo luận với lãnh đạo.

Ví dụ ◨ có sơ đồ

Heatmap tô đỏ năng lực 'Customer Management' và 'Channel Management' (yếu, ưu tiên cao) trên bản đồ ba tầng — lãnh đạo nhìn một cái là thấy nên đầu tư vào đâu.

Câu hỏi thường gặpBản đồ năng lực nghiệp vụ chia thành mấy tầng?

Ba tầng: Strategic (định hướng), Core (tạo giá trị trực tiếp) và Supporting (hỗ trợ).

Heatmap dùng để làm gì?

Tô màu các năng lực trên bản đồ để làm nổi bật năng lực nào yếu/cần đầu tư, giúp lãnh đạo nhanh chóng thấy nên ưu tiên vào đâu.

Value stream → Capability nghĩa là gì?

Là ánh xạ từng chặng của dòng giá trị (value stream) tới các năng lực nghiệp vụ cần thiết để thực hiện chặng đó.

**Mạch nối:** Kiến trúc nghiệp vụ đã xong. Chu trình chuyển sang Phase C — phát triển kiến trúc Hệ thống Thông tin gồm Dữ liệu và Ứng dụng.

### Phase C: Information Systems Architecture (Objectives)

**Mô tả nội dung**

Hai mục tiêu: (1) Phát triển Kiến trúc Hệ thống Thông tin Mục tiêu (Kiến trúc Dữ liệu & Ứng dụng) mô tả cách chúng cho phép hiện thực hóa Kiến trúc Nghiệp vụ và Tầm nhìn, xử lý được Statement of Architecture Work và mối quan tâm stakeholder; (2) Nhận diện thành phần lộ trình ứng viên dựa trên khoảng cách Baseline–Target của kiến trúc Hệ thống Thông tin.

**Diễn giải chi tiết**

Phase C phát triển kiến trúc Hệ thống Thông tin — gồm hai miền con: Dữ liệu và Ứng dụng. Vị trí của nó trong ADM rất logic: sau khi biết nghiệp vụ cần vận hành thế nào (Phase B), giờ xác định cần dữ liệu gì và ứng dụng nào để hiện thực hóa nghiệp vụ đó. Mục tiêu là xây kiến trúc Dữ liệu & Ứng dụng mục tiêu 'cho phép' (enable) kiến trúc nghiệp vụ — nghĩa là chúng tồn tại để phục vụ nghiệp vụ, không phải mục đích tự thân. Như mọi phase, Phase C cũng so Baseline với Target để tìm khoảng cách và tạo thành phần lộ trình. TOGAF cho phép làm Data trước hay Application trước tùy bối cảnh, nhưng cả hai phải gắn kết.

**Ví dụ**

Phase C của WMS: kiến trúc dữ liệu định nghĩa thực thể 'Tồn kho', 'Vị trí lưu'; kiến trúc ứng dụng định nghĩa module 'quản lý tồn kho' và 'điều phối xuất/nhập' — tất cả để phục vụ quy trình kho mục tiêu ở Phase B.

Câu hỏi thường gặpPhase C phát triển kiến trúc gì?

Kiến trúc Hệ thống Thông tin, gồm hai miền con: Kiến trúc Dữ liệu và Kiến trúc Ứng dụng.

Vì sao Phase C đứng sau Phase B?

Vì phải biết nghiệp vụ cần vận hành thế nào (B) trước, rồi mới xác định dữ liệu và ứng dụng nào cần có (C) để hiện thực hóa nghiệp vụ đó.

**Mạch nối:** Sau mục tiêu, slide tiếp theo liệt kê các đầu ra của Phase C — các thành phần kiến trúc Hệ thống Thông tin cho lộ trình.

### Phase C: Information Architecture (Output)

**Mô tả nội dung**

Đầu ra là các thành phần Kiến trúc Thông tin (Dữ liệu & Ứng dụng) của một Lộ trình Kiến trúc, kèm danh sách gợi ý các thành phần kiến trúc cần tạo trong miền này.

**Diễn giải chi tiết**

Tương tự Phase B, đầu ra của Phase C là bộ thành phần mô tả kiến trúc Dữ liệu và Ứng dụng, sẽ ghép vào Lộ trình Kiến trúc tổng thể. Chúng gồm mô tả Baseline/Target của cả hai miền con, kết quả phân tích khoảng cách, các thành phần lộ trình ứng viên, và phần cập nhật vào Architecture Definition Document cùng Requirements Specification. Danh sách gợi ý các tạo phẩm (như Danh mục Thực thể Dữ liệu, Ma trận Dữ liệu–Ứng dụng, Danh mục Ứng dụng, Sơ đồ Giao tiếp Ứng dụng…) giúp kiến trúc sư tạo tài liệu đầy đủ và nhất quán. Những đầu ra này là nguyên liệu cho Phase E khi xây lộ trình.

**Ví dụ**

Đầu ra Phase C gồm: danh mục thực thể dữ liệu, ma trận CRUD (ứng dụng nào tạo/đọc/sửa/xóa dữ liệu nào), danh mục ứng dụng mục tiêu, và các thành phần lộ trình như 'xây API tồn kho thời gian thực'.

Câu hỏi thường gặpĐầu ra của Phase C là gì?

Các thành phần Kiến trúc Dữ liệu & Ứng dụng của Lộ trình Kiến trúc — mô tả Baseline/Target, gap analysis và các thành phần lộ trình ứng viên.

Ma trận Dữ liệu–Ứng dụng để làm gì?

Để thể hiện ứng dụng nào tạo/đọc/sửa/xóa (CRUD) dữ liệu nào — giúp thấy phụ thuộc và trùng lắp giữa ứng dụng và dữ liệu.

**Mạch nối:** Slide tiếp theo nhắc lại và củng cố mục tiêu của Phase C trước khi đi sâu vào từng miền con Dữ liệu và Ứng dụng.

### Phase C: Information Architecture (nhắc lại mục tiêu)

**Mô tả nội dung**

Nhắc lại hai mục tiêu của Phase C: phát triển Kiến trúc Hệ thống Thông tin Mục tiêu (Dữ liệu & Ứng dụng) cho phép hiện thực hóa Kiến trúc Nghiệp vụ và Tầm nhìn; và nhận diện thành phần lộ trình ứng viên dựa trên khoảng cách Baseline–Target.

**Diễn giải chi tiết**

Slide này lặp lại mục tiêu Phase C như một 'điểm neo' trước khi tách ra trình bày chi tiết hai miền con — Dữ liệu (slides 45–46) và Ứng dụng (slide 47). Việc nhắc lại nhấn mạnh một nguyên tắc: dù chia thành Dữ liệu và Ứng dụng, cả hai luôn phục vụ cùng một mục đích — cho phép kiến trúc nghiệp vụ và tầm nhìn thành hiện thực. Điều này giúp kiến trúc sư không sa đà vào chi tiết kỹ thuật của từng miền mà quên mất mục tiêu nghiệp vụ chung.

**Ví dụ**

Trước khi thiết kế chi tiết cơ sở dữ liệu tồn kho, kiến trúc sư tự nhắc: mọi thực thể dữ liệu này tồn tại để phục vụ quy trình kho mục tiêu, không phải để 'đẹp về mặt kỹ thuật'.

Câu hỏi thường gặpVì sao mục tiêu Phase C được nhắc lại?

Để neo lại định hướng — dù tách thành miền Dữ liệu và Ứng dụng, cả hai đều phục vụ cùng mục đích cho phép kiến trúc nghiệp vụ và tầm nhìn thành hiện thực.

**Mạch nối:** Slide tiếp theo phân định rạch ròi hai miền con của Phase C và cảnh báo hai hiểu lầm phổ biến về Dữ liệu và Ứng dụng.

### Information Architectures = Data + Application

**Mô tả nội dung**

Kiến trúc Thông tin gồm Kiến trúc Dữ liệu và Kiến trúc Ứng dụng. Dữ liệu: định nghĩa các loại và nguồn dữ liệu chính cần để hỗ trợ nghiệp vụ — Kiến trúc Dữ liệu KHÔNG phải Thiết kế CSDL. Ứng dụng: định nghĩa các loại hệ thống ứng dụng chính để xử lý dữ liệu và hỗ trợ nghiệp vụ — Kiến trúc Ứng dụng KHÔNG phải Thiết kế Ứng dụng, và Ứng dụng KHÔNG chỉ là PHẦN MỀM.

**Diễn giải chi tiết**

Slide này gỡ hai hiểu lầm quan trọng, giúp kiến trúc sư giữ đúng tầm 'kiến trúc' chứ không sa vào 'thiết kế'. Thứ nhất, Kiến trúc Dữ liệu định nghĩa các LOẠI và NGUỒN dữ liệu chính ở mức khái niệm/logic — nó KHÔNG phải thiết kế cơ sở dữ liệu (bảng, cột, khóa). Thứ hai, Kiến trúc Ứng dụng định nghĩa các LOẠI hệ thống ứng dụng ở mức nhóm năng lực — nó KHÔNG phải thiết kế ứng dụng (code, giao diện), và quan trọng: 'ứng dụng' không đồng nghĩa với 'phần mềm' mà là các nhóm năng lực logic xử lý dữ liệu và hỗ trợ nghiệp vụ. Sự phân biệt kiến trúc–thiết kế này giữ cho EA ở mức ổn định, độc lập công nghệ, trong khi thiết kế chi tiết được để cho giai đoạn triển khai.

**Ví dụ**

Kiến trúc Dữ liệu nói 'cần dữ liệu Khách hàng, Đơn hàng, Tồn kho' (loại & nguồn), còn thiết kế CSDL mới quyết bảng nào, cột nào — kiến trúc sư dừng ở mức đầu, để mức sau cho đội phát triển.

Câu hỏi thường gặpKiến trúc Dữ liệu có phải Thiết kế CSDL không?

Không — Kiến trúc Dữ liệu định nghĩa các loại và nguồn dữ liệu chính ở mức khái niệm/logic, không phải thiết kế bảng/cột/khóa của cơ sở dữ liệu.

'Ứng dụng' trong Kiến trúc Ứng dụng có phải chỉ là phần mềm không?

Không — ứng dụng là các nhóm năng lực logic xử lý dữ liệu và hỗ trợ nghiệp vụ, không chỉ là phần mềm cụ thể.

**Mạch nối:** Sau khi phân định, slide tiếp theo đi sâu vào miền con đầu tiên — Kiến trúc Dữ liệu và các khía cạnh của nó.

### Data Architecture – Kiến trúc Dữ liệu

**Mô tả nội dung**

Áp khuôn 9 bước chung, kèm các khía cạnh dữ liệu: trạng thái dữ liệu (at rest, in motion, in use, open data); meta model (data entity, logical/physical data component); quản lý dữ liệu (định nghĩa rõ, hiểu cách sử dụng, biết nơi tạo/lưu/vận chuyển, mức độ phức tạp, tích hợp); di trú dữ liệu (nhận diện yêu cầu, mức độ chuyển đổi/làm sạch cần thiết); và quản trị dữ liệu (cấu trúc, hệ thống quản lý, con người).

**Diễn giải chi tiết**

Kiến trúc Dữ liệu bao quát dữ liệu ở nhiều trạng thái và góc độ. Về trạng thái: dữ liệu tĩnh (at rest — lưu trong CSDL), dữ liệu đang di chuyển (in motion — truyền giữa hệ thống), dữ liệu đang dùng (in use — đang xử lý), và dữ liệu mở (open data). Meta model định nghĩa các thành phần dữ liệu ở mức logic (data entity, logical data component) và vật lý (physical data component). Quản lý dữ liệu đòi hỏi định nghĩa rõ ràng, hiểu cách thực thể dữ liệu được sử dụng, biết nơi dữ liệu được tạo/lưu/vận chuyển, đánh giá mức phức tạp và nhu cầu tích hợp. Di trú dữ liệu nhận diện yêu cầu chuyển đổi và mức độ làm sạch/'weeding' cần thiết. Cuối cùng, quản trị dữ liệu (data governance) đảm bảo có cấu trúc, hệ thống quản lý và con người chịu trách nhiệm. Đây là miền ngày càng quan trọng khi dữ liệu trở thành tài sản chiến lược.

Ví dụ ◨ có sơ đồ

Khi di trú sang WMS mới, kiến trúc dữ liệu xác định: dữ liệu tồn kho cũ cần làm sạch (loại bỏ SKU trùng), ánh xạ sang cấu trúc mới, và ai (data steward) chịu trách nhiệm chất lượng dữ liệu sau di trú.

Câu hỏi thường gặpDữ liệu có những trạng thái nào?

Data at rest (lưu trữ), in motion (đang truyền), in use (đang xử lý) và open data (dữ liệu mở).

Quản trị dữ liệu (data governance) gồm những gì?

Cấu trúc quản trị, hệ thống quản lý và con người chịu trách nhiệm — đảm bảo dữ liệu được định nghĩa, quản lý và sử dụng đúng.

Di trú dữ liệu quan tâm điều gì?

Nhận diện yêu cầu di trú và mức độ chuyển đổi, làm sạch (weeding & cleansing) dữ liệu cần thiết khi chuyển sang hệ thống mới.

**Mạch nối:** Slide tiếp theo trình bày các bước cụ thể của Kiến trúc Dữ liệu và ba mức mô hình dữ liệu: Conceptual, Logical, Physical.

### Data Architecture Steps – Conceptual / Logical / Physical

**Mô tả nội dung**

Áp khuôn 9 bước (chọn mô hình → Baseline → Target → gap → thành phần lộ trình → giải quyết tác động → rà soát → hoàn thiện → cập nhật ADD), với ba mức mô hình dữ liệu: CONCEPTUAL ('The What' – cái gì), LOGICAL ('The How' – như thế nào), PHYSICAL ('With what' – bằng gì).

**Diễn giải chi tiết**

Kiến trúc Dữ liệu được phát triển qua ba mức trừu tượng giảm dần — một kỹ thuật kinh điển trong mô hình hóa dữ liệu. Mức Conceptual ('The What') trả lời 'cần những dữ liệu gì' ở mức nghiệp vụ: các thực thể chính và quan hệ, không quan tâm công nghệ (ví dụ Khách hàng, Đơn hàng, Sản phẩm). Mức Logical ('The How') làm rõ cấu trúc chi tiết hơn: thuộc tính, khóa, chuẩn hóa — vẫn độc lập với hệ quản trị CSDL cụ thể. Mức Physical ('With what') mới ánh xạ xuống công nghệ cụ thể: bảng, kiểu dữ liệu, chỉ mục trên một hệ CSDL nhất định. Kiến trúc sư EA chủ yếu làm việc ở mức Conceptual và Logical; mức Physical thuộc về thiết kế và triển khai. Ba mức này bảo đảm dữ liệu được suy nghĩ từ nghiệp vụ xuống kỹ thuật một cách nhất quán.

**Ví dụ**

Conceptual: 'Khách hàng có nhiều Đơn hàng'. Logical: thực thể Customer (id, tên, email), Order (id, ngày, tổng tiền), quan hệ 1–n. Physical: bảng customers, orders trên PostgreSQL với chỉ mục cụ thể.

Câu hỏi thường gặpBa mức mô hình dữ liệu là gì?

Conceptual ('The What' – cần dữ liệu gì), Logical ('The How' – cấu trúc chi tiết) và Physical ('With what' – hiện thực trên công nghệ cụ thể).

Kiến trúc sư EA làm việc ở mức nào?

Chủ yếu ở mức Conceptual và Logical; mức Physical thuộc về thiết kế và triển khai.

**Mạch nối:** Xong Dữ liệu, slide tiếp theo chuyển sang miền con thứ hai của Phase C — Kiến trúc Ứng dụng.

### Application Architecture – Kiến trúc Ứng dụng

**Mô tả nội dung**

Áp khuôn 9 bước, dùng các mô hình nghiệp vụ và ứng dụng chung liên quan đến ngành, cùng mô hình ứng dụng cho các chức năng nghiệp vụ cấp cao phổ biến (thương mại điện tử, quản lý chuỗi cung ứng…). Ứng dụng được mô tả KHÔNG như hệ thống máy tính mà như các nhóm năng lực logic quản lý các đối tượng dữ liệu (Data Architecture) và hỗ trợ chức năng nghiệp vụ (Business Architecture). Ứng dụng ổn định, ít đổi theo thời gian; còn công nghệ hiện thực chúng thì thay đổi.

**Diễn giải chi tiết**

Kiến trúc Ứng dụng định nghĩa các ứng dụng như những nhóm NĂNG LỰC LOGIC — không phải các hệ thống máy tính cụ thể. Đây là điểm then chốt: một 'ứng dụng' trong kiến trúc là tập hợp năng lực quản lý các đối tượng dữ liệu (từ Kiến trúc Dữ liệu) và hỗ trợ chức năng nghiệp vụ (từ Kiến trúc Nghiệp vụ), được mô tả độc lập với công nghệ cụ thể. Lý do quan trọng: các ứng dụng (ở mức năng lực logic) ỔN ĐỊNH và ít thay đổi theo thời gian, trong khi CÔNG NGHỆ hiện thực chúng thì đổi liên tục theo xu hướng và nhu cầu. Tách bạch 'ứng dụng logic' khỏi 'công nghệ hiện thực' giúp kiến trúc bền vững: ta có thể thay công nghệ (đổi từ on-premise sang cloud) mà không phá vỡ bản đồ ứng dụng logic. Có thể dùng các mô hình tham chiếu theo ngành để không phải sáng tạo lại từ đầu.

**Ví dụ**

Ứng dụng 'Quản lý Tồn kho' (năng lực logic) ổn định qua nhiều năm, dù công nghệ hiện thực nó đổi từ phần mềm desktop → web → microservices cloud — bản đồ ứng dụng logic không đổi.

Câu hỏi thường gặpỨng dụng trong Kiến trúc Ứng dụng được mô tả thế nào?

Như các nhóm năng lực logic quản lý đối tượng dữ liệu và hỗ trợ chức năng nghiệp vụ, độc lập với công nghệ cụ thể — không phải hệ thống máy tính.

Vì sao tách 'ứng dụng logic' khỏi 'công nghệ hiện thực'?

Vì ứng dụng logic ổn định theo thời gian, còn công nghệ đổi liên tục — tách ra giúp thay công nghệ mà không phá vỡ bản đồ ứng dụng.

**Mạch nối:** Kiến trúc Hệ thống Thông tin (Dữ liệu & Ứng dụng) đã xong. Chu trình chuyển sang Phase D — nền tảng công nghệ chạy tất cả.

### Phase D: Technology Architecture – Kiến trúc Công nghệ

**Mô tả nội dung**

Phát triển Kiến trúc Công nghệ Mục tiêu cho phép các khối kiến trúc nghiệp vụ, dữ liệu và ứng dụng được bàn giao qua các thành phần công nghệ (technology components) và dịch vụ công nghệ (technology services), theo cách xử lý được Statement of Architecture Work và mối quan tâm stakeholder. Nhận diện thành phần lộ trình ứng viên dựa trên khoảng cách Baseline–Target.

**Diễn giải chi tiết**

Phase D là tầng nền dưới cùng của BDAT: nó xác định hạ tầng công nghệ (phần cứng, phần mềm nền, mạng, nền tảng) cần có để chạy các ứng dụng và dữ liệu đã thiết kế ở Phase C, từ đó hiện thực hóa nghiệp vụ ở Phase B. Kiến trúc Công nghệ mô tả các thành phần công nghệ và dịch vụ công nghệ 'cho phép' bàn giao các khối kiến trúc của ba miền trên. Vị trí cuối cùng trong chuỗi phát triển kiến trúc (B→C→D) phản ánh nguyên tắc 'nghiệp vụ dẫn dắt, công nghệ theo sau': ta chỉ chọn công nghệ sau khi đã rõ cần làm gì (nghiệp vụ), cần dữ liệu và ứng dụng gì (thông tin). Như mọi phase, Phase D cũng so Baseline–Target để tìm khoảng cách và tạo thành phần lộ trình.

**Ví dụ**

Phase D của WMS: chọn nền tảng cloud, cơ sở dữ liệu phân tán, hạ tầng IoT cho thiết bị quét mã — những công nghệ cần thiết để chạy ứng dụng WMS đã thiết kế ở Phase C.

Câu hỏi thường gặpPhase D phát triển kiến trúc gì?

Kiến trúc Công nghệ Mục tiêu — hạ tầng và dịch vụ công nghệ cho phép các khối nghiệp vụ, dữ liệu và ứng dụng được bàn giao.

Vì sao Phase D đứng cuối chuỗi B→C→D?

Vì theo nguyên tắc 'nghiệp vụ dẫn dắt, công nghệ theo sau' — chỉ chọn công nghệ sau khi đã rõ nghiệp vụ, dữ liệu và ứng dụng cần gì.

**Mạch nối:** Slide tiếp theo liệt kê các đầu ra của Phase D — hoàn tất bộ ba kiến trúc B, C, D làm nguyên liệu cho lộ trình.

### Phase D: Technology Architecture (Outputs)

**Mô tả nội dung**

Đầu ra là các thành phần Kiến trúc Công nghệ của một Lộ trình Kiến trúc, kèm danh sách gợi ý các thành phần kiến trúc cần tạo trong miền công nghệ.

**Diễn giải chi tiết**

Đầu ra Phase D hoàn tất bộ ba thành phần kiến trúc (Nghiệp vụ + Thông tin + Công nghệ) sẽ được lắp ráp thành Lộ trình ở Phase E. Chúng gồm mô tả Baseline/Target của kiến trúc công nghệ, kết quả gap analysis, các thành phần lộ trình ứng viên, và cập nhật vào Architecture Definition Document cùng Requirements Specification. Danh sách gợi ý các tạo phẩm (như Danh mục Nền tảng Công nghệ, Ma trận Ứng dụng–Công nghệ, Sơ đồ Môi trường & Vị trí…) giúp mô tả đầy đủ hạ tầng mục tiêu. Đến đây, ba miền B–C–D đã cung cấp đủ 'nguyên liệu' để Phase E bắt đầu lắp ráp bức tranh lộ trình tổng thể.

**Ví dụ**

Đầu ra Phase D gồm: danh mục công nghệ chuẩn (cloud provider, DB engine), ma trận ứng dụng–hạ tầng, và thành phần lộ trình như 'di trú hạ tầng lên cloud giai đoạn 1'.

Câu hỏi thường gặpĐầu ra của Phase D là gì?

Các thành phần Kiến trúc Công nghệ của Lộ trình Kiến trúc — mô tả Baseline/Target, gap analysis và thành phần lộ trình ứng viên.

Sau Phase D, ADM đi tiếp đến đâu?

Đến Phase E — nơi lắp ráp các thành phần từ B, C, D thành Lộ trình Kiến trúc tổng thể.

**Mạch nối:** Ba miền kiến trúc đã hoàn tất. Chu trình bước vào Phase E — nơi biến các thành phần rời rạc thành một lộ trình khả thi.

### Phase E: Opportunities & Solutions (Objectives)

**Mô tả nội dung**

Ba mục tiêu: (1) Tạo phiên bản hoàn chỉnh đầu tiên của Lộ trình Kiến trúc, dựa trên gap analysis và các thành phần lộ trình ứng viên từ Phase B, C, D; (2) Xác định có cần cách tiếp cận tăng dần (incremental) không, và nếu có thì nhận diện các Kiến trúc Chuyển tiếp (Transition Architectures) mang lại giá trị kinh doanh liên tục; (3) Định nghĩa các Solution Building Blocks (SBB) để hoàn thiện Kiến trúc Mục tiêu dựa trên các ABB.

**Diễn giải chi tiết**

Phase E là bước ngoặt: từ 'thiết kế kiến trúc' (B–D) sang 'lập kế hoạch thực thi'. Nó gom mọi khoảng cách và thành phần lộ trình ứng viên từ ba miền lại, tạo ra phiên bản hoàn chỉnh đầu tiên của Lộ trình Kiến trúc. Một quyết định quan trọng ở đây: có nên đi tăng dần (incremental) không? Nếu 'nhảy một bước' từ hiện tại tới mục tiêu quá rủi ro, kiến trúc sư định nghĩa các Kiến trúc Chuyển tiếp (Transition Architectures) — những trạng thái trung gian, mỗi trạng thái đã mang lại giá trị kinh doanh thực. Đồng thời, Phase E chuyển từ ABB (khối kiến trúc logic) sang SBB (khối giải pháp cụ thể) — bắt đầu trả lời 'dùng giải pháp gì để hiện thực'. Đây là nơi kiến trúc bắt đầu 'chạm đất'.

**Ví dụ**

Thay vì triển khai toàn bộ WMS mới trong một lần (rủi ro cao), Phase E chia thành 3 Transition Architecture: (1) số hóa nhập kho, (2) thêm xuất kho tự động, (3) tích hợp thời gian thực — mỗi bước đã tạo giá trị.

Câu hỏi thường gặpMục tiêu chính của Phase E là gì?

Tạo phiên bản hoàn chỉnh đầu tiên của Lộ trình Kiến trúc từ gap analysis của B, C, D; xác định Kiến trúc Chuyển tiếp nếu cần; và định nghĩa các SBB.

Transition Architecture là gì?

Các trạng thái kiến trúc trung gian giữa Baseline và Target, mỗi trạng thái đã mang lại giá trị kinh doanh — dùng khi đi tăng dần thay vì nhảy một bước.

ABB và SBB khác nhau thế nào?

ABB (Architecture Building Block) là khối logic độc lập công nghệ; SBB (Solution Building Block) là khối giải pháp cụ thể hiện thực hóa ABB.

**Mạch nối:** Để tạo lộ trình, cần hợp nhất và gom nhóm các kết quả từ B–D. Slide tiếp theo trình bày quá trình Hợp nhất & Tổng hợp (Consolidation & Aggregation).

### Consolidation and Aggregation – Hợp nhất & Tổng hợp

**Mô tả nội dung**

Chuỗi việc: xác định/xác nhận các thuộc tính thay đổi cấp doanh nghiệp; xác định ràng buộc nghiệp vụ cho triển khai; rà soát & hợp nhất kết quả gap analysis từ Phase B–D; rà soát yêu cầu hợp nhất xuyên nghiệp vụ; hợp nhất & dung hòa yêu cầu tương tác (interoperability); tinh chỉnh & xác nhận phụ thuộc; xác nhận mức sẵn sàng & rủi ro; xây Chiến lược Triển khai & Di trú; nhận diện & gom các gói công việc chính; nhận diện Kiến trúc Chuyển tiếp; tạo Lộ trình Kiến trúc & Kế hoạch Triển khai & Di trú.

**Diễn giải chi tiết**

Đây là 'công xưởng lắp ráp' của Phase E: biến hàng loạt khoảng cách rời rạc từ ba miền thành một lộ trình mạch lạc. Quá trình gồm nhiều bước hợp nhất: gom kết quả gap analysis của cả B, C, D lại; hợp nhất các yêu cầu xuyên nghiệp vụ và yêu cầu tương tác (interoperability) giữa các hệ thống; tinh chỉnh và xác nhận các phụ thuộc (cái gì phải làm trước cái gì); xác nhận lại mức sẵn sàng và rủi ro. Từ đó hình thành Chiến lược Triển khai & Di trú, các gói công việc (work packages) được gom nhóm hợp lý, các Kiến trúc Chuyển tiếp, và cuối cùng là Lộ trình Kiến trúc cùng Kế hoạch Triển khai & Di trú. Bước gom nhóm và xác định phụ thuộc chính là nơi 'trình tự tốt nhất' của lộ trình được quyết định.

**Ví dụ**

Ba miền cho ra 20 khoảng cách rời rạc; Phase E gom chúng thành 5 gói công việc, sắp theo phụ thuộc (chuẩn hóa dữ liệu phải trước tích hợp ứng dụng), thành một lộ trình có trình tự hợp lý.

Câu hỏi thường gặpConsolidation & Aggregation làm gì?

Hợp nhất kết quả gap analysis và yêu cầu từ Phase B–D, dung hòa yêu cầu tương tác, xác nhận phụ thuộc, rồi gom thành gói công việc và Lộ trình Kiến trúc.

Vì sao phải xác định phụ thuộc?

Vì phụ thuộc quyết định trình tự — việc nào phải làm trước việc nào — để lộ trình khả thi và không bị nghẽn.

**Mạch nối:** Slide tiếp theo liệt kê các đầu ra cụ thể của Phase E — Lộ trình Kiến trúc và Kế hoạch Triển khai & Di trú.

### Phase E: Opportunities & Solutions (Outputs)

**Mô tả nội dung**

Đầu ra có thể gồm: Lộ trình Kiến trúc (Architecture Roadmap) — bao gồm các Gói Công việc (kèm phụ thuộc, giá trị), các Kiến trúc Chuyển tiếp, và khuyến nghị triển khai (ví dụ SBB); và Kế hoạch Triển khai & Di trú (bản nháp) kèm Chiến lược Triển khai & Di trú.

**Diễn giải chi tiết**

Đầu ra Phase E là hai sản phẩm cốt lõi cho việc thực thi. Thứ nhất, Lộ trình Kiến trúc — 'bản đồ đường đi' từ hiện tại tới mục tiêu, gồm các Gói Công việc (mỗi gói có phụ thuộc và giá trị kinh doanh rõ ràng), các Kiến trúc Chuyển tiếp (các trạm dừng trung gian) và khuyến nghị triển khai (như dùng SBB nào). Thứ hai, Kế hoạch Triển khai & Di trú (bản nháp) cùng Chiến lược đi kèm — cách thức di chuyển thực tế. Đây vẫn là 'bản nháp' vì Phase F sẽ hoàn thiện chi tiết. Điểm quan trọng: mỗi gói công việc gắn với giá trị kinh doanh cụ thể, giúp việc ưu tiên và xin ngân sách ở Phase F trở nên dễ dàng và có căn cứ.

**Ví dụ**

Lộ trình gồm 5 gói: Gói 1 'chuẩn hóa dữ liệu tồn kho' (giá trị: nền tảng cho mọi gói sau); Gói 2 'API thời gian thực'... mỗi gói ghi rõ phụ thuộc và giá trị để lãnh đạo ưu tiên.

Câu hỏi thường gặpĐầu ra chính của Phase E là gì?

Lộ trình Kiến trúc (gồm gói công việc, Kiến trúc Chuyển tiếp, khuyến nghị triển khai) và Kế hoạch Triển khai & Di trú (bản nháp) kèm Chiến lược.

Vì sao mỗi gói công việc cần gắn giá trị?

Để việc ưu tiên và xin ngân sách ở Phase F có căn cứ rõ ràng — biết gói nào đáng đầu tư trước.

**Mạch nối:** Lộ trình đã hình thành nhưng đi kèm rủi ro. Slide tiếp theo nhấn mạnh vai trò quản lý rủi ro xuyên suốt lộ trình.

### Risk Management – Quản lý Rủi ro (tối đa lợi ích, tối thiểu tổn thất)

DF

**Mô tả nội dung**

Quản lý rủi ro nhằm tối đa hóa lợi ích kinh doanh và tối thiểu hóa tổn thất kinh doanh — được thực hiện xuyên suốt lộ trình và quá trình chuyển đổi.

**Diễn giải chi tiết**

Slide này nhắc rằng quản lý rủi ro không phải một bước riêng lẻ mà là hoạt động xuyên suốt, gắn với lộ trình vừa xây. Mục đích kép: tối đa hóa lợi ích kinh doanh (nắm bắt cơ hội) đồng thời tối thiểu hóa tổn thất (phòng ngừa thất bại). Trong bối cảnh lộ trình EA, rủi ro tồn tại ở nhiều chỗ: rủi ro kỹ thuật (công nghệ chưa trưởng thành), rủi ro tổ chức (kháng cự thay đổi), rủi ro phụ thuộc (một gói trễ kéo theo cả chuỗi), rủi ro tài chính. Cách tiếp cận đã nêu ở slide 31 (ma trận Tác động × Tần suất) được áp dụng liên tục: nhận diện, đánh giá, giảm thiểu và theo dõi rủi ro qua từng giai đoạn triển khai. Quản lý rủi ro tốt là điều phân biệt một lộ trình 'trên giấy' với một lộ trình thực sự khả thi.

**Ví dụ**

Lộ trình xác định rủi ro 'gói API trễ do thiếu chuyên gia' — giảm thiểu bằng thuê ngoài dự phòng; rủi ro được theo dõi qua mỗi giai đoạn thay vì chỉ đánh giá một lần đầu.

Câu hỏi thường gặpMục đích của quản lý rủi ro trong EA là gì?

Tối đa hóa lợi ích kinh doanh đồng thời tối thiểu hóa tổn thất kinh doanh, xuyên suốt lộ trình và quá trình chuyển đổi.

Rủi ro trong lộ trình EA thường nằm ở đâu?

Rủi ro kỹ thuật, tổ chức (kháng cự thay đổi), phụ thuộc (một gói trễ kéo cả chuỗi) và tài chính.

**Mạch nối:** Với rủi ro trong tầm kiểm soát, lộ trình cần được hoàn thiện thành kế hoạch di trú chi tiết. Đó là nội dung Phase F ở slide tiếp theo.

### Phase F: Migration Planning – Lập kế hoạch Di trú

**Mô tả nội dung**

Ba mục tiêu chính: hoàn thiện Lộ trình Kiến trúc và Kế hoạch Triển khai & Di trú; đảm bảo kế hoạch được phối hợp với cách tổ chức quản lý thay đổi trong danh mục thay đổi tổng thể; đảm bảo stakeholder then chốt hiểu rõ giá trị kinh doanh và chi phí của các gói công việc và Kiến trúc Chuyển tiếp. Bảy bước gồm: xác nhận tương tác khung quản lý; gán giá trị kinh doanh cho mỗi gói; ước lượng nguồn lực/thời gian/phương tiện bàn giao; ưu tiên các dự án di trú qua đánh giá chi phí–lợi ích & xác nhận rủi ro; xác nhận lộ trình & cập nhật ADD; hoàn tất kế hoạch; hoàn tất chu kỳ phát triển & ghi bài học kinh nghiệm.

**Diễn giải chi tiết**

Phase F biến lộ trình 'phác thảo' của Phase E thành một kế hoạch di trú chi tiết, khả thi và được ưu tiên. Ba mục tiêu: hoàn thiện kế hoạch; phối hợp nó với danh mục thay đổi tổng thể của doanh nghiệp (để dự án EA không xung đột với các sáng kiến khác); và đảm bảo stakeholder hiểu rõ giá trị và chi phí của từng gói. Bảy bước cụ thể tập trung vào việc 'định lượng': gán giá trị kinh doanh cho mỗi gói, ước lượng nguồn lực và thời gian, rồi ưu tiên các dự án di trú dựa trên đánh giá chi phí–lợi ích và rủi ro. Bước cuối rất đáng chú ý: hoàn tất chu kỳ và GHI BÀI HỌC KINH NGHIỆM — thể hiện tinh thần cải tiến liên tục của ADM, mỗi vòng lặp làm giàu kinh nghiệm cho vòng sau.

**Ví dụ**

Phase F gán giá trị và chi phí cho 5 gói, ước lượng nguồn lực, rồi xếp thứ tự ưu tiên bằng phân tích chi phí–lợi ích; đồng thời kiểm tra không trùng lịch với dự án nâng cấp ERP đang chạy.

Câu hỏi thường gặpPhase F khác Phase E ở điểm nào?

Phase E tạo lộ trình phác thảo; Phase F hoàn thiện nó thành kế hoạch di trú chi tiết, được định lượng (giá trị, chi phí, nguồn lực) và ưu tiên.

Vì sao phải phối hợp với danh mục thay đổi tổng thể?

Để dự án EA không xung đột hay chồng lịch với các sáng kiến thay đổi khác của doanh nghiệp.

Bước cuối 'ghi bài học kinh nghiệm' thể hiện điều gì?

Tinh thần cải tiến liên tục của ADM — mỗi vòng lặp làm giàu kinh nghiệm cho các vòng sau.

**Mạch nối:** Slide tiếp theo trình bày cách tiếp cận di trú qua các chiều con người, dữ liệu/vật lý và công cụ 'ma trận thay đổi'.

### Approach: Migration Planning & The Matrix of Change

**Mô tả nội dung**

Cách tiếp cận lập kế hoạch di trú xét trên các chiều: People (con người) và Physical/Data (vật lý & dữ liệu), sử dụng công cụ 'The Matrix of Change' (Ma trận Thay đổi).

**Diễn giải chi tiết**

Slide này giới thiệu góc nhìn thực tế về di trú: thay đổi không chỉ là kỹ thuật mà còn chạm tới con người và các tài sản vật lý/dữ liệu. 'The Matrix of Change' là công cụ phân tích các thành phần cần thay đổi và mối quan hệ giữa chúng — cái nào bổ trợ nhau (nên đổi cùng lúc), cái nào xung đột (cần xử lý thứ tự), cái nào ổn định (giữ lại). Nó giúp trả lời các câu hỏi khó của di trú: nên đổi tất cả cùng lúc (big bang) hay từng phần? Thứ tự nào ít gây gián đoạn nhất? Chiều con người (People) đặc biệt quan trọng — di trú thành công về kỹ thuật vẫn có thể thất bại nếu con người không được chuẩn bị. Công cụ này bổ sung cho việc lập kế hoạch di trú một lăng kính về tính khả thi và sự gián đoạn.

**Ví dụ**

Ma trận Thay đổi cho thấy 'đổi hệ thống kho' và 'đổi quy trình làm việc của nhân viên kho' bổ trợ nhau — nên triển khai đồng thời kèm đào tạo, thay vì đổi hệ thống trước rồi mới đào tạo sau.

Câu hỏi thường gặpThe Matrix of Change dùng để làm gì?

Phân tích các thành phần cần thay đổi và quan hệ giữa chúng (bổ trợ, xung đột, ổn định) để quyết định nên đổi cùng lúc hay từng phần, và theo thứ tự nào.

Vì sao chiều 'con người' quan trọng trong di trú?

Vì di trú thành công về kỹ thuật vẫn có thể thất bại nếu con người không được chuẩn bị và đào tạo phù hợp.

**Mạch nối:** Kế hoạch di trú đã sẵn sàng. Chu trình chuyển sang giai đoạn triển khai và giám sát — Phase G.

### Phase G: Implementation Governance (Objectives)

DF

**Mô tả nội dung**

Hai mục tiêu: (1) Đảm bảo các dự án triển khai TUÂN THỦ Kiến trúc Mục tiêu; (2) Thực hiện các chức năng Quản trị Kiến trúc phù hợp cho giải pháp và cho bất kỳ Yêu cầu Thay đổi Kiến trúc nào phát sinh từ triển khai.

**Diễn giải chi tiết**

Phase G là 'người gác cổng' của quá trình triển khai — nó đảm bảo những gì thực sự được xây khớp với kiến trúc mục tiêu đã thiết kế. Hai mục tiêu bổ sung nhau. Thứ nhất, đảm bảo tuân thủ (conformance): các dự án triển khai (thường do đội phát triển hoặc nhà thầu thực hiện) phải bám sát kiến trúc mục tiêu, không 'đi chệch' vì tiện lợi trước mắt. Thứ hai, thực hiện quản trị kiến trúc (Architecture Governance): xử lý các Yêu cầu Thay đổi Kiến trúc phát sinh trong quá trình triển khai một cách có kiểm soát — vì thực tế luôn khác kế hoạch, và một số thay đổi là hợp lý cần được phê duyệt chính thức. Phase G là nơi 'bản thiết kế' gặp 'thực tế thi công', và vai trò quản trị đảm bảo hai bên không tách rời.

**Ví dụ**

Đội phát triển WMS muốn dùng một CSDL khác cho tiện; Phase G yêu cầu họ tuân thủ chuẩn kiến trúc, hoặc nếu có lý do chính đáng thì nộp Yêu cầu Thay đổi Kiến trúc để hội đồng xem xét.

Câu hỏi thường gặpMục tiêu của Phase G là gì?

Đảm bảo các dự án triển khai tuân thủ Kiến trúc Mục tiêu, và thực hiện quản trị kiến trúc cho giải pháp cùng các Yêu cầu Thay đổi phát sinh.

Vì sao cần Phase G?

Vì thực tế thi công luôn có xu hướng đi chệch bản thiết kế; Phase G giám sát để những gì được xây khớp với kiến trúc mục tiêu.

**Mạch nối:** Sau mục tiêu, slide tiếp theo trình bày các bước cụ thể của Implementation Governance.

### Implementation Governance (Steps)

DF

**Mô tả nội dung**

Sáu bước: xác nhận phạm vi & ưu tiên triển khai với ban quản lý phát triển; nhận diện nguồn lực & kỹ năng triển khai; hướng dẫn phát triển các giải pháp triển khai; thực hiện rà soát Tuân thủ Kiến trúc Doanh nghiệp; triển khai vận hành nghiệp vụ và IT; thực hiện rà soát sau triển khai và đóng dự án.

**Diễn giải chi tiết**

Sáu bước của Phase G dẫn dắt việc triển khai từ khởi đầu tới khi đóng. Bắt đầu bằng việc chốt phạm vi và ưu tiên với ban quản lý phát triển, rồi nhận diện nguồn lực và kỹ năng cần thiết. Trong quá trình phát triển, kiến trúc sư đóng vai hướng dẫn (guide) chứ không làm thay. Then chốt là bước rà soát Tuân thủ Kiến trúc (Architecture Compliance review) — kiểm tra chính thức xem giải pháp có khớp kiến trúc không. Sau khi triển khai vận hành cả nghiệp vụ lẫn IT, bước cuối là rà soát sau triển khai (post-implementation review) và đóng dự án — đánh giá kết quả thực so với kỳ vọng. Chuỗi bước này đảm bảo triển khai được kiểm soát về chất lượng kiến trúc từ đầu đến cuối.

**Ví dụ**

Trước khi go-live WMS, kiến trúc sư thực hiện Compliance Review: kiểm tra hệ thống đã xây có dùng đúng chuẩn API, đúng CSDL chuẩn, đúng mô hình bảo mật đã thiết kế hay không.

Câu hỏi thường gặpRà soát Tuân thủ Kiến trúc (Compliance Review) là gì?

Kiểm tra chính thức xem giải pháp được triển khai có khớp với kiến trúc mục tiêu đã thiết kế hay không.

Vai trò của kiến trúc sư trong triển khai là gì?

Là hướng dẫn (guide) và giám sát tuân thủ, không phải làm thay đội phát triển.

**Mạch nối:** Slide tiếp theo đào sâu hơn vào cơ chế quản trị triển khai và những vấn đề thường gặp khi con người hiểu sai kế hoạch.

### Implementation / Governance (chi tiết)

DF

**Mô tả nội dung**

Nhấn mạnh: đảm bảo mọi người tuân theo kế hoạch và công việc của họ khớp với Kiến trúc Mục tiêu; vấn đề nảy sinh khi con người hiểu sai kế hoạch. Cơ chế gồm: thiết lập chương trình triển khai bàn giao các Kiến trúc Chuyển tiếp; áp dụng lịch triển khai theo giai đoạn phản ánh ưu tiên kinh doanh trong Lộ trình; tuân theo chuẩn quản trị doanh nghiệp/IT/kiến trúc; dùng phương pháp quản lý danh mục/chương trình hiện có; định nghĩa khung vận hành để đảm bảo giải pháp sống lâu dài.

**Diễn giải chi tiết**

Slide này làm rõ 'con người' là mắt xích dễ gãy nhất của triển khai: vấn đề thường nảy sinh không phải vì kế hoạch sai mà vì con người HIỂU SAI kế hoạch. Vì thế quản trị triển khai phải đảm bảo hai điều: mọi người tuân theo kế hoạch, và công việc thực tế của họ khớp với kiến trúc mục tiêu. Các cơ chế hỗ trợ gồm: thiết lập chương trình triển khai để bàn giao các Kiến trúc Chuyển tiếp; áp lịch triển khai theo giai đoạn phản ánh ưu tiên kinh doanh; tuân theo các chuẩn quản trị sẵn có (doanh nghiệp, IT, kiến trúc); tận dụng phương pháp quản lý danh mục/chương trình hiện hành thay vì phát minh lại; và định nghĩa một khung vận hành (operations framework) để đảm bảo giải pháp tồn tại bền vững sau khi bàn giao. Điểm nhấn: triển khai tốt là sự kết hợp giữa kỷ luật tuân thủ và giao tiếp rõ ràng để tránh hiểu sai.

**Ví dụ**

Đội phát triển hiểu sai 'tích hợp thời gian thực' thành 'đồng bộ mỗi 5 phút'; Compliance Review và giao tiếp rõ ràng phát hiện và sửa sự hiểu sai trước khi nó thành lỗi kiến trúc.

Câu hỏi thường gặpVấn đề lớn nhất trong triển khai theo slide này là gì?

Con người hiểu sai kế hoạch — nên quản trị phải đảm bảo mọi người tuân theo kế hoạch và công việc khớp kiến trúc mục tiêu.

'Operations framework' để làm gì?

Để đảm bảo giải pháp được triển khai tồn tại bền vững, vận hành hiệu quả trong suốt vòng đời dài của nó.

**Mạch nối:** Sau khi triển khai, kiến trúc mới phải được duy trì và thích nghi khi hoàn cảnh đổi. Đó là nhiệm vụ của Phase H — Quản lý Thay đổi Kiến trúc.

### Phase H: Architecture Change Management

**Mô tả nội dung**

Ba mục tiêu: (1) Đảm bảo chu kỳ phát triển kiến trúc được duy trì; (2) Đảm bảo Khung Quản trị Kiến trúc được thực thi (đối với các thay đổi); (3) Đảm bảo Năng lực EA đáp ứng yêu cầu hiện tại. Kèm châm ngôn: 'Kế hoạch thì vô giá trị, nhưng việc lập kế hoạch là tất cả' và 'Hỗn loạn & phức tạp dẫn dắt vũ trụ, nên bạn cần có kế hoạch cho nó'.

**Diễn giải chi tiết**

Phase H đóng vòng ADM và biến nó thành một chu trình sống động. Nó không để kiến trúc 'đóng băng' sau triển khai mà đảm bảo kiến trúc tiếp tục tiến hóa khi doanh nghiệp và môi trường thay đổi. Ba mục tiêu: duy trì chu kỳ phát triển kiến trúc (giữ EA sống); thực thi Khung Quản trị Kiến trúc đối với mọi thay đổi (thay đổi phải qua kiểm soát, không tùy tiện); và đảm bảo Năng lực EA luôn đáp ứng yêu cầu hiện tại. Hai châm ngôn nắm bắt tinh thần cốt lõi: 'kế hoạch vô giá trị nhưng việc lập kế hoạch là tất cả' (giá trị nằm ở quá trình suy nghĩ và chuẩn bị, không phải ở tài liệu tĩnh) và 'hỗn loạn dẫn dắt vũ trụ nên phải có kế hoạch cho nó' (chấp nhận thay đổi là tất yếu và chuẩn bị cho nó). Phase H phân biệt hai loại thay đổi: thay đổi nhỏ (xử lý qua quản lý thay đổi) và thay đổi lớn (kích hoạt một chu kỳ ADM mới).

**Ví dụ**

Sau go-live WMS, một quy định pháp lý mới về truy xuất nguồn gốc xuất hiện; Phase H đánh giá đây là thay đổi lớn và kích hoạt một chu kỳ ADM mới để cập nhật kiến trúc.

Câu hỏi thường gặpMục tiêu của Phase H là gì?

Duy trì chu kỳ phát triển kiến trúc; thực thi Khung Quản trị Kiến trúc với các thay đổi; đảm bảo Năng lực EA đáp ứng yêu cầu hiện tại.

Phase H xử lý thay đổi thế nào?

Phân biệt thay đổi nhỏ (xử lý qua quản lý thay đổi) và thay đổi lớn (kích hoạt một chu kỳ ADM mới).

Ý nghĩa câu 'kế hoạch vô giá trị nhưng lập kế hoạch là tất cả'?

Giá trị nằm ở quá trình suy nghĩ và chuẩn bị chứ không ở tài liệu tĩnh — vì thực tế luôn thay đổi, khả năng thích nghi quan trọng hơn bản kế hoạch cố định.

**Mạch nối:** Xuyên suốt tám phase là một hoạt động trung tâm không ngừng nghỉ. Slide tiếp theo trình bày Quản lý Yêu cầu — trái tim của ADM.

### ADM Requirements Management Phase – Quản lý Yêu cầu

**Mô tả nội dung**

Ba việc: đảm bảo quy trình Quản lý Yêu cầu được duy trì và vận hành cho mọi phase ADM liên quan; quản lý các yêu cầu kiến trúc phát sinh trong bất kỳ lần thực thi chu kỳ/phase nào; đảm bảo yêu cầu kiến trúc liên quan luôn sẵn có cho mỗi phase khi được thực thi. Nhấn mạnh: vòng tròn Quản lý Yêu cầu KHÔNG phải tập yêu cầu tĩnh, mà là một quy trình ĐỘNG — yêu cầu được nhận diện, lưu trữ, đưa vào/lấy ra khỏi các phase và giữa các chu kỳ.

**Diễn giải chi tiết**

Quản lý Yêu cầu (Requirements Management) nằm ở TRUNG TÂM chu trình ADM — không phải một phase tuần tự mà là hoạt động vận hành liên tục, kết nối với mọi phase. Ba nhiệm vụ: duy trì quy trình cho mọi phase; quản lý các yêu cầu phát sinh bất cứ lúc nào trong chu kỳ; và đảm bảo yêu cầu đúng luôn sẵn sàng cho phase đang chạy. Điểm nhấn quan trọng nhất: đây là quy trình ĐỘNG chứ không tĩnh. Yêu cầu không được 'khóa cứng' một lần rồi thôi, mà liên tục được nhận diện mới, lưu trữ, đưa vào và lấy ra khỏi các phase, thậm chí truyền giữa các chu kỳ ADM. Chính vì thế nó ở trung tâm bánh xe: mọi phase đều 'nạp' yêu cầu từ đây và 'trả' yêu cầu mới về đây. Đây là cơ chế giúp ADM thích nghi với thay đổi thay vì cứng nhắc.

Ví dụ ◨ có sơ đồ

Khi làm Phase C, đội phát hiện một yêu cầu mới về bảo mật dữ liệu; yêu cầu này được đưa vào Requirements Management, rồi 'nạp' cho Phase D và cả các chu kỳ sau — không bị thất lạc.

Câu hỏi thường gặpRequirements Management nằm ở đâu trong ADM?

Ở trung tâm chu trình — không phải một phase tuần tự mà là hoạt động vận hành liên tục kết nối với mọi phase.

Vì sao gọi Quản lý Yêu cầu là quy trình 'động'?

Vì yêu cầu liên tục được nhận diện mới, lưu trữ, đưa vào/lấy ra khỏi các phase và truyền giữa các chu kỳ — không phải một tập yêu cầu tĩnh khóa cứng một lần.

**Mạch nối:** Ngoài các phase và quản lý yêu cầu, có một miền xuyên suốt cả kiến trúc cần được quan tâm đặc biệt. Slide tiếp theo giới thiệu Kiến trúc An toàn (Security Architecture).

### Security Architecture – Kiến trúc An toàn (xuyên suốt)

**Mô tả nội dung**

Là cấu trúc các thành phần tổ chức, khái niệm, logic và vật lý tương tác mạch lạc để đạt và duy trì trạng thái rủi ro được quản lý và an toàn thông tin. Vừa là động lực vừa là yếu tố cho phép hành vi an toàn, bền bỉ, tin cậy. Kiến trúc An toàn tương tác với cả bốn miền BDAT nên gọi là 'cross-cutting'. EA và ESA bổ trợ nhau; hai quy trình lõi: Quản lý An toàn Thông tin (ISM) và Quản lý Rủi ro Doanh nghiệp (ERM); mỗi tạo phẩm an toàn gắn với một phase ADM (Preliminary → A–H). Rủi ro luôn được dẫn dắt top-down từ đánh giá giá trị kinh doanh.

**Diễn giải chi tiết**

Kiến trúc An toàn (Security Architecture) là miền đặc biệt vì nó KHÔNG nằm ở một tầng riêng mà xuyên suốt (cross-cutting) cả bốn miền BDAT — mọi thành phần nghiệp vụ, dữ liệu, ứng dụng, công nghệ đều có khía cạnh an toàn. Nó vừa là động lực (thúc đẩy hành vi an toàn) vừa là yếu tố cho phép (làm cho hệ thống bền bỉ, tin cậy). Enterprise Security Architecture (ESA) bổ trợ và nâng cao EA. Hai quy trình lõi: Quản lý An toàn Thông tin (ISM) lo việc bảo vệ thông tin, và Quản lý Rủi ro Doanh nghiệp (ERM) lo rủi ro tổng thể. Điểm tinh tế: mỗi tạo phẩm an toàn được nhúng vào một phase ADM cụ thể (từ Preliminary tới A–H) — nghĩa là an toàn không phải việc 'làm sau cùng' mà được tích hợp vào mọi giai đoạn. Và rủi ro luôn được dẫn dắt TOP-DOWN từ đánh giá giá trị kinh doanh: ta bảo vệ cái gì và bao nhiêu tùy theo giá trị kinh doanh của nó.

**Ví dụ**

Khi thiết kế WMS, an toàn được nhúng ngay từ Phase A (nguyên tắc bảo mật), Phase C (mã hóa dữ liệu tồn kho nhạy cảm), Phase D (kiểm soát truy cập hạ tầng) — không đợi đến khi xong mới 'gắn bảo mật vào'.

Câu hỏi thường gặpVì sao Kiến trúc An toàn được gọi là 'cross-cutting'?

Vì nó tương tác với cả bốn miền BDAT (Business, Data, Application, Technology) chứ không nằm riêng một tầng.

Hai quy trình lõi của Kiến trúc An toàn là gì?

Quản lý An toàn Thông tin (ISM) và Quản lý Rủi ro Doanh nghiệp (ERM).

Rủi ro an toàn được dẫn dắt theo hướng nào?

Top-down — từ đánh giá giá trị kinh doanh: bảo vệ cái gì và mức độ nào tùy theo giá trị kinh doanh của nó.

**Mạch nối:** Slide tiếp theo đi sâu vào quy trình quản lý rủi ro của Kiến trúc An toàn và danh mục dịch vụ an toàn.

### Security Architecture: The Risk Management Process

**Mô tả nội dung**

Quy trình quản lý rủi ro là một vòng đời liên tục, nhúng sâu vào mọi hoạt động nghiệp vụ: Thiết lập Bối cảnh → Đánh giá Rủi ro (Nhận diện → Phân tích → Định giá) → Xử lý Rủi ro; xuyên suốt là Giao tiếp & Tư vấn và Theo dõi & Rà soát. Các kiểm soát được gom thành dịch vụ an toàn tái sử dụng (Security Services Catalog): Quản lý Danh tính & Truy cập (ai được làm gì, khi nào); Quản lý Liên tục (giữ vận hành); Tình báo An toàn (phân tích, đo lường, báo cáo); Quản lý Tuân thủ (đáp ứng nghĩa vụ & kiểm soát).

**Diễn giải chi tiết**

Slide này chi tiết hóa cách quản lý rủi ro an toàn theo một vòng đời chuẩn (dựa trên ISO 31000). Quy trình gồm: Thiết lập Bối cảnh (xác định phạm vi, tiêu chí rủi ro) → Đánh giá Rủi ro với ba bước con Nhận diện (rủi ro nào tồn tại) → Phân tích (khả năng và hậu quả) → Định giá (so với tiêu chí để quyết định xử lý) → Xử lý Rủi ro (chấp nhận, giảm thiểu, chuyển giao hay né tránh). Xuyên suốt vòng đời là hai hoạt động liên tục: Giao tiếp & Tư vấn (với stakeholder) và Theo dõi & Rà soát (vì rủi ro thay đổi). Điểm thực dụng quan trọng: các biện pháp kiểm soát được đóng gói thành các dịch vụ an toàn TÁI SỬ DỤNG trong một Security Services Catalog — như Quản lý Danh tính & Truy cập, Quản lý Liên tục, Tình báo An toàn, Quản lý Tuân thủ. Cách 'dịch vụ hóa' này giúp mọi dự án dùng chung các năng lực an toàn thay vì mỗi dự án tự làm lại.

**Ví dụ**

Thay vì mỗi ứng dụng tự xây đăng nhập riêng, doanh nghiệp dùng dịch vụ 'Identity & Access Management' dùng chung trong catalog — mọi hệ thống mới chỉ việc 'gọi' dịch vụ này.

Câu hỏi thường gặpCác bước của quy trình quản lý rủi ro an toàn là gì?

Thiết lập Bối cảnh → Đánh giá Rủi ro (Nhận diện → Phân tích → Định giá) → Xử lý Rủi ro, với Giao tiếp & Tư vấn và Theo dõi & Rà soát xuyên suốt.

Security Services Catalog là gì?

Danh mục các dịch vụ an toàn tái sử dụng (như Quản lý Danh tính & Truy cập, Quản lý Liên tục, Tình báo An toàn, Quản lý Tuân thủ) để mọi dự án dùng chung thay vì tự làm lại.

**Mạch nối:** Module 2 đã trình bày đầy đủ phương pháp TOGAF ADM và các phase. Khóa học bước vào Module 3 — bộ kỹ thuật cụ thể giúp thực thi ADM hiệu quả.
